#!/usr/bin/env bash

git init
pipenv install --dev pre-commit black isort flake8
