# {{ cookiecutter.repo_name }}


## Installation

This package may be installed using pip:
```
pip install git+{{ cookiecutter.github_url }}.git
```


## Dev

Create an environment using the dev-environment.yml packaged with the repository:
```
conda env create -f dev-environment.yml
```
Activate your environment:
```
conda activate {{ cookiecutter.repo_name }}-dev
```

Install editable package:
```
pip install -e .
```

Tests can be executed from the root directory using:
```
pytest .
```

### Note
This README was automatically generated using the template defined in https://github.com/jacquelinegarrahan/python-project-template with the following configuration:

```json
{
    "author": "{{ cookiecutter.author }}",
    "email": "{{ cookiecutter.email }}",
    "github_username": "{{ cookiecutter.github_username }}",
    "github_url": "{{ cookiecutter.github_url }}",
    "project_name": "{{ cookiecutter.project_name }}", 
    "repo_name": "{{ cookiecutter.repo_name }}", 
    "package": "{{ cookiecutter.package }}",
}
```
