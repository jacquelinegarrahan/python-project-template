#!/usr/bin/env bash

versioneer install --vendor


git init $(pwd)
git add .
git  commit -a -m  "Initial Cookiecutter commit"