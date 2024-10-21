.PHONY: run

SHELL := /bin/bash

activate:
	@source venv/bin/activate

activate-fish:
	@source venv/bin/activate.fish

run:
	. .env
	@flask run --debug --port=8081

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
