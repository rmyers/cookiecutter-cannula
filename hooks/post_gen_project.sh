#!/bin/bash

make setup
make generate args=--force

echo ""
echo "{{cookiecutter.project_slug}} Setup Successfully!"
echo "Get started:"
echo ""
make