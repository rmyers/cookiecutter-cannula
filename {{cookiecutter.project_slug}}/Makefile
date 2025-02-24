#% _________________________________________________
#%      _________    _   ___   ____  ____    ___
#%     / ____/   |  / | / / | / / / / / /   /   |
#%    / /   / /| | /  |/ /  |/ / / / / /   / /| |
#%   / /___/ ___ |/ /|  / /|  / /_/ / /___/ ___ |
#%   \____/_/  |_/_/ |_/_/ |_/\____/_____/_/  |_|
#% _________________________________________________
#%
#% Tools for building, running, and testing cannula applications.
#%
#% Usage:
#%   make <command>
#%
#% Getting Started:
#%   make setup
#%   make run
#%
#% Available Commands:

REQUIREMENTS		:= pyproject.toml
SHELL				:= /bin/bash
VIRTUAL_ENV			:= venv
PYTHON				:= $(shell command -v python3 || command -v python)

# PHONY just means this target does not make any files
.PHONY: setup clean test help

default: help

# Make sure the virtualenv exists, create it if not.
$(VIRTUAL_ENV):
	$(PYTHON) -m venv $(VIRTUAL_ENV)

# Check for the existence/timestamp of .reqs-installed if the
# file is missing or older than the pyproject.toml this will run pip
$(VIRTUAL_ENV)/.reqs-installed: $(REQUIREMENTS)
	$(VIRTUAL_ENV)/bin/pip install -e .
	touch $(VIRTUAL_ENV)/.reqs-installed

setup: $(VIRTUAL_ENV) $(VIRTUAL_ENV)/.reqs-installed ## Setup local environment

clean: ## Clean your local workspace
	rm -rf $(VIRTUAL_ENV)
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -f db.sqlite
	find . -name '*.py[co]' -delete

test: setup  ## Test the code
	$(VIRTUAL_ENV)/bin/pytest

format:  ## Format the code with ruff
	$(VIRTUAL_ENV)/bin/ruff format {{cookiecutter.project_slug}} tests

mypy: setup ## Run mypy on code
	$(VIRTUAL_ENV)/bin/mypy ./{{cookiecutter.project_slug}}

run: setup  ## Run the application
	$(VIRTUAL_ENV)/bin/python -m {{cookiecutter.project_slug}} run

generate: setup  ## Run cannula codegen on the project. Pass args like (make generate args='--force')
	$(VIRTUAL_ENV)/bin/cannula codegen $(args)

initdb: setup  ## Create database tables
	$(VIRTUAL_ENV)/bin/python -m {{cookiecutter.project_slug}} initdb

addusers: setup  ## Add test users
	$(VIRTUAL_ENV)/bin/python -m {{cookiecutter.project_slug}} addusers

help: ## Show the available commands
	@grep '^#%' $(MAKEFILE_LIST) | sed -e 's/#%//'
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | awk -F ':.*?## ' 'NF==2 {printf "   %-20s%s\n", $$1, $$2}' | sort
