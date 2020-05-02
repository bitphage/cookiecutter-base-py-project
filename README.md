# Cookiecutter Template for Python Project

This is a basic template with minimal features.

## Features

* poetry for package management
* pre-commit hooks:
  * Linting with [flake8](https://flake8.pycqa.org/en/latest/) (+ plugins)
  * Remove unused imports and variables with [autoflake](https://github.com/myint/autoflake)
  * Sorting imports with [isort](https://github.com/timothycrosley/isort)
  * Code formatting with [black](https://black.readthedocs.io/en/stable/)
  * Docstrings formatting with [docformatter](https://github.com/myint/docformatter)
  * Static type checking with [mypy](https://mypy.readthedocs.io/)
* pytest
* sphinx + [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/) for automatic API documentation

## Setup

Install [cruft](https://github.com/timothycrosley/cruft/) or [cookiecutter](https://github.com/cookiecutter/cookiecutter)

```
cruft create <url>
```

or

```
cookiecutter <url>
```
