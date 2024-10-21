.PHONY: run

activate:
	@source venv/bin/activate

activate-fish:
	@source venv/bin/activate.fish

run:
	@flask --app src/main run --host=0.0.0.0 --port=8081 --debug

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
