#!/usr/bin/env bash

git init
virtualenv -p python3.7 --prompt="({{ cookiecutter.project_name }}) " {{ cookiecutter.virtualenv }}
{{ cookiecutter.virtualenv }}/bin/python -m pip install -U pip
{{ cookiecutter.virtualenv }}/bin/python -m pip install -r requirements.txt
{{ cookiecutter.virtualenv }}/bin/python -m pre_commit install
{{ cookiecutter.virtualenv }}/bin/python setup.py develop
