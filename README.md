# Cookiecutter Template for Python Project

This is a basic template with minimal features.

## Features

* [poetry](https://github.com/python-poetry/poetry) for package management
* [pre-commit](https://pre-commit.com/) hooks:
  * Linting with [flake8](https://flake8.pycqa.org/en/latest/) (+ plugins)
  * Remove unused imports and variables with [autoflake](https://github.com/myint/autoflake)
  * Sorting imports with [isort](https://github.com/timothycrosley/isort)
  * Code formatting with [black](https://black.readthedocs.io/en/stable/)
  * Docstrings formatting with [docformatter](https://github.com/myint/docformatter)
  * Static type checking with [mypy](https://mypy.readthedocs.io/)
* [pytest](https://docs.pytest.org/en/latest/) + [pytest-cov](https://pytest-cov.readthedocs.io/) + [pytest-mock](https://github.com/pytest-dev/pytest-mock)
* [sphinx](https://www.sphinx-doc.org/) + [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/) for automatic API documentation
* [github actions](https://help.github.com/en/actions):
  * Run *pre-commit* checks on PRs
  * Run pytest on commits and PRs

## Setup

Install [cruft](https://github.com/timothycrosley/cruft/) or [cookiecutter](https://github.com/cookiecutter/cookiecutter)

```
cruft create <url>
```

or

```
cookiecutter <url>
```
