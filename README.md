# Cookiecutter Template for Python Project

This is a basic template with minimal features.

## Features

* Pipenv-oriented
* pre-commit hooks which calls:
  * Linting with [flake8](https://flake8.pycqa.org/en/latest/) (+ plugins)
  * Sorting imports with [isort](https://github.com/timothycrosley/isort)
  * Code formatting with [black](https://black.readthedocs.io/en/stable/)
  * Docstrings formatting with [docformatter](https://github.com/myint/docformatter)
  * Static type checking with [mypy](https://mypy.readthedocs.io/)

## Setup

Install [cruft](https://github.com/timothycrosley/cruft/) or [cookiecutter](https://github.com/cookiecutter/cookiecutter)

```
cruft create <url>
```

or

```
cookiecutter <url>
```
