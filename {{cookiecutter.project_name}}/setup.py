from setuptools import setup, find_packages


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
    packages=find_packages(exclude=("tests",)),
    requires_python=">=3.7",
    {%- if cookiecutter.url %}
    url="{{ cookiecutter.url }}",
    {% endif -%}
    license="{{ cookiecutter.license }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)