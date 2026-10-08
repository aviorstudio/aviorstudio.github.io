SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.PHONY: help install lint test build check dev stop clean
help:
	@echo "make check: validate and build the static redirect"
install:
	mise trust .mise.toml
	mise install python actionlint
lint:
	mise exec -- python3 scripts/check.py
	mise exec -- actionlint
build:
	mise exec -- python3 scripts/check.py --build
check: lint build
test dev stop:
	@echo "$@: unsupported: static redirect configuration; lint checks all redirect mechanisms"
clean:
	python3 -c 'import shutil; shutil.rmtree(".artifacts", ignore_errors=True)'
