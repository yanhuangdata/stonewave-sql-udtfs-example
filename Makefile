default_target: all

all : install black_format test build

install: 
	poetry install

test:
	poetry run pytest

black_format:
	poetry run black -l 120 example_func && poetry run black -l 120 tests

build: install
	poetry run python gen_version.py && poetry run python gen_func_info.py && rm -rf dist && poetry build -vvv
