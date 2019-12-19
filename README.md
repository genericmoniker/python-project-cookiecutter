# Python Project Cookiecutter

## Features
- Dependency and package management with [poetry](https://python-poetry.org/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)

## How to use
```sh
# Install pipx if poetry and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install poetry using pipx
pipx install poetry

# Use cookiecutter to create project from this template, following prompts
# for project-specific settings
pipx run cookiecutter gh:genericmoniker/python-project-cookiecutter

# Enter project directory
cd <repo_name>

# Initialize git repo
git init
git add --all

# Follow "Development setup" steps in the newly created README.md
```

## Justifications

* package_name - Why "newproject" instead of "new-project" (same as the repo
  name)? [PEP
  8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
* pylint - Why not flake8? I've found that in combination with black, flake8
  doesn't offer much. 

## Credits

Inspired by [sourceryai/python-best-practices-cookiecutter](https://github.com/search?q=sourceryai%2Fpython-best-practices-cookiecutter).
