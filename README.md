# Oldies Station

A modern FastAPI project template with pre-configured tooling and best practices. This template provides a solid foundation for building Python web applications with FastAPI.

## Technologies

This template includes the following technologies and tools:

- **[FastAPI](https://fastapi.tiangolo.com/)** (>=0.120.4) - Modern, fast web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** (>=0.38.0) - Lightning-fast ASGI server
- **[Ruff](https://docs.astral.sh/ruff/)** (>=0.14.3) - Fast Python linter and formatter
- **[pre-commit](https://pre-commit.com/)** (>=4.3.0) - Git hook framework for code quality
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver

### Requirements

- Python >= 3.12
- uv (recommended for dependency management)

## Getting Started

### Installation

1. Clone this repository:
```bash
git clone https://github.com/carvalhocaio/oldies-station
cd oldies-station
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Install pre-commit hooks:
```bash
uv run pre-commit install
```

## Available Commands

This project includes a Makefile with convenient commands:

### `make run`
Starts the development server with hot reload on port 8000.
```bash
make run
```
The API will be available at `http://localhost:8000`

### `make lint`
Runs code quality checks using Ruff.
```bash
make lint
```
Executes: `ruff check . && ruff check . --diff`

### `make format`
Automatically fixes linting issues and formats code.
```bash
make format
```
Executes: `ruff check . --fix && ruff format .`

## Pre-commit Hooks

This template comes with pre-commit hooks configured to run `make lint` before every commit. This ensures code quality is maintained throughout development.

To manually run pre-commit on all files:
```bash
uv run pre-commit run --all-files
```

## Project Structure

```
.
├── main.py                    # FastAPI application entry point
├── pyproject.toml             # Project dependencies and metadata
├── ruff.toml                  # Ruff linter/formatter configuration
├── Makefile                   # Development commands
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## Ruff Configuration

The project uses Ruff with the following settings:

- **Line length**: 79 characters
- **Indent width**: 4 spaces (tabs)
- **Quote style**: Double quotes
- **Selected rules**: Import sorting (I), Pyflakes (F), Pycodestyle (E), Pylint (PL), Pytest style (PT)

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
