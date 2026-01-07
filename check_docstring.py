#!/usr/bin/env python3

import ast
import sys
from pathlib import Path
import subprocess


class DocstringChecker(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.missing = []

    def visit_FunctionDef(self, node):
        if ast.get_docstring(node) is None:
            self.missing.append(
                ("function", node.name, node.lineno)
            )
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        if ast.get_docstring(node) is None:
            self.missing.append(
                ("async function", node.name, node.lineno)
            )
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if ast.get_docstring(node) is None:
            self.missing.append(
                ("class", node.name, node.lineno)
            )
        self.generic_visit(node)


def check_file(path):
    try:
        if str(path) == "check_docstring.py":
            return
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=path)
    except SyntaxError as e:
        print(f"[ERREUR] {path} : erreur de syntaxe ligne {e.lineno}")
        return

    checker = DocstringChecker(path)
    checker.visit(tree)

    if checker.missing:
        print(f"\n📄 {path}")
        for kind, name, line in checker.missing:
            print(f"  - {kind} '{name}' sans docstring (ligne {line})")
    else:
        print(f"\n📄 {path} : OK (toutes les docstrings sont présentes)")


def main():
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        if target.is_file() and target.suffix == ".py":
            check_file(target)
    else:
        target = Path(".")
        for py_file in target.rglob("*.py"):
            check_file(py_file)
    print("\nRunning flake8...")
    subprocess.run("flake8")


if __name__ == "__main__":
    main()
