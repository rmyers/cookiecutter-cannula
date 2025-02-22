#!/bin/bash

make setup
make generate args=--force

echo -n "\n\n{{cookiecutter.project_slug}} Setup Successfully!"
echo -n "Commands:\n\trun: make run\n\thelp: make"