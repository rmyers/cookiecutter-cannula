#!/bin/bash

echo "Installing Dependencies"
make setup
echo "Generating Code"
make generate args=--force
echo "{{cookiecutter.project_slug}} Setup Successfully!"
make