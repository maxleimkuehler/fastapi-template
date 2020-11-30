# Thanks to Mark Warneke (warneke.mark@gmail.com) for this makefile.

.EXPORT_ALL_VARIABLES:
current_dir=$(shell pwd)

SRC='src'

VENV_PATH='env/bin/activate'
ENVIRONMENT_VARIABLE_FILE?=.env

DOCKER_NAME='fast-api-template'
DOCKER_TAG?='1.0'
LOGLEVEL?=WARNING

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)


init: ## sets up environment and installs requirements
init: install
	pip install -r requirements.txt

install: ## Installs development requirments
install:
	python -m pip install --upgrade pip
	# Used for linting
	pip install flake8
	# Used for testing
	pip install pytest
	# Install autopep8
	pip install autopep8

	pip install mypy pycodestyle pydocstyle

format: ## Formats the code with autopep8
format:
	autopep8 $(SRC) --recursive --in-place --pep8-passes 2000 --aggressive --verbose

lint: ## Runs flake8 on src, exit if critical rules are broken
lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHfub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics

lint2:
	pylint --rcfile=.pylintrc $(SRC) -f parseable -r n && \
	mypy --silent-imports $(SRC) && \
	pycodestyle $(SRC) --max-line-length=120 && \
	pydocstyle $(SRC)

clean: ## Remove build and cache files
clean:
	rm -rf *.egg-info
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache
	
	find . -name '*.pyc' | rm -rf
	find . -name '*.pyo' | rm -rf

	# Remove all pycache
	find . | grep -E "__pycache__" | xargs rm -rf

test: ## Run pytest
test:
	pytest . -p no:logging -p no:warnings

leave: ## Cleanup and deactivate venv
leave: clean
	deactivate

build: ## Build docker image
build:
	docker build -f Dockerfile.dev -t fast-api-template .

run: ## build, start and run docker image
run: # remove 
	docker run --name $(DOCKER_NAME) --volume="$(current_dir)/src:/app" --env-file .docker.env -p 8080:8080 $(DOCKER_NAME)

run.d: ## build, start and run docker image
run.d: # remove 
	docker run --name $(DOCKER_NAME) --volume="$(current_dir)/src:/app" --env-file .docker.env -d -p 8080:8080 $(DOCKER_NAME)
	@echo "Open browser http://localhost:80/docs"

exec: ## build, start and exec into docker image
exec: start
	docker exec -it $(DOCKER_NAME) python

stop: ## stop docker container fastapi
stop: 
	docker stop $(DOCKER_NAME)

remove: ## remove docker container fastapi
remove: stop
	docker rm -f $(DOCKER_NAME)

logs: ## Returns the current docker logs
logs:
	docker logs --follow $(DOCKER_NAME) 