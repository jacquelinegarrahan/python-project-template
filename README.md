# python-project-template
A cookiecutter template for quickly formatting a starting point for development with my standard/preferred tools. 

## Use 

Create a .json file:
```
{
    "author": "Jacqueline Garrahan",
    "email": "jacquelinegarrahan@gmail.com",
    "github_username": "jacquelinegarrahan",
    "github_url": "https://github.com/jacquelinegarrahan/test_cookiecutter_project.git",
    "project_name": "My Package", 
    "repo_name": "{{ cookiecutter.project_name.lower().replace(' ', '-') }}", 
    "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
}
```


## Tools
* conda
* click for cli dev
* versioneer (cookiecutter runs install during post-installation hook)
* [pre-commit](https://pre-commit.com/) hook with black and flake8
* pytest with coverage
* Common github actions
* [pydantic](https://pydantic-docs.helpmanual.io/) for use with data structures
* docs
    * mkdocs
    * mkdocstrings
