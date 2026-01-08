# Docstring Checker & flake8 Runner

A small Python script that scans Python files and reports missing docstrings for **functions, async functions, and classes**, then runs **flake8** on the project.

This tool is intended for simple code quality checks and educational use.

---

## What This Script Does

- Parses Python files using the built-in `ast` module
- Detects missing docstrings for:
  - Functions (`def`)
  - Async functions (`async def`)
  - Classes (`class`)
- Prints a per-file report of missing docstrings
- Runs `flake8` after the docstring checks

---

## Requirements

- Python 3.8+
- `flake8`

Install flake8 if needed:

```bash
pip install flake8
```

## Usage

- Check a single Python file
```bash
python check_docstring.py my_file.py
```
Only the specified file will be checked.

- Check all Python files recursively
```bash
python check_docstring.py
```
This scans all .py files in the current directory and its subdirectories.

- The script automatically skips itself (check_docstring.py).

Example Output
```console
📄 example.py

- function 'add' sans docstring (ligne 10)
- class 'Parser' sans docstring (ligne 25)

📄 utils.py : OK (toutes les docstrings sont présentes)

Running flake8...
utils.py:3:1: F401 'os' imported but unused
```

Error Handling

If a file contains a syntax error, it is reported and skipped:

```console
[ERREUR] bad_file.py : erreur de syntaxe ligne 14```

Other files continue to be processed.
