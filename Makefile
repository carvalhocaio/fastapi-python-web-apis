run:
	uv run uvicorn main:app --reload --port 8000

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .
