# {{ cookiecutter.repo_name }}


## Installation

This package may be installed using pip:
```
pip install git+{{ cookiecutter.github_url }}.git
```


## Dev

Create an environment using the environment.yml packaged with the repository:
```
conda env create -f environment.yml
```
Activate your environment:
```
conda activate {{ cookiecutter.project_slug }}
```
Install dev requirements:
```
conda install --file dev-requirements.txt
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
This README was automatically generated using the template defined in https://github.com/slaclab/lume-services/lume_services/modeling/templating with the following configuration:

```json
{
    "author": "{{ cookiecutter.author }}",
    "email": "{{ cookiecutter.email }}",
    "github_username": "{{ cookiecutter.github_username }}",
    "github_url": "{{ cookiecutter.github_url }}",
    "project_name": "{{ cookiecutter.project_name }}", 
    "repo_name": "{{ cookiecutter.repo_name }}", 
    "project_slug": "{{ cookiecutter.project_slug }}",
}
```
