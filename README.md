# Randomizer API

A production-ready FastAPI application for generating random numbers and managing randomizable item lists. This project demonstrates modern Python API development with a modular architecture, SQLite database, environment-based configuration, comprehensive logging, and professional development practices.

## Features

### Random Number Generation
- Generate random numbers up to a maximum value
- Generate random numbers within a specific range (min-max)
- Input validation and error handling
- Comprehensive logging of all operations

### Item Management
- **CRUD Operations**: Create, Read, Update, Delete items
- **SQLite Database**: In-memory database for fast operations
- **Pagination**: Configurable pagination (21 items per page by default)
- **Data Validation**: Pydantic models with field validation
- **Duplicate Detection**: Unique constraints enforced at database level
- **Randomized Ordering**: Get items in both original and shuffled order

### Architecture & Infrastructure
- **Modular Structure**: Organized codebase with separation of concerns
- **Environment Configuration**: python-decouple for flexible settings
- **Structured Logging**: Loguru with console and file output
- **CORS Middleware**: Configured for cross-origin requests
- **API Documentation**: Auto-generated Swagger UI and ReDoc
- **REST Client Testing**: Comprehensive test suite in `client.http`

## Tech Stack

- **Python 3.10+**
- **FastAPI** - Modern, fast web framework
- **SQLite** - In-memory database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **python-decouple** - Environment-based configuration
- **Loguru** - Structured logging
- **uv** - Fast Python package installer

## Installation

### Prerequisites
- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer (recommended)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/carvalhocaio/fastapi-python-web-apis
cd fastapi-python-web-apis
```

2. **Create and activate virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

Using uv (recommended):
```bash
uv pip install -r pyproject.toml
```

Or using pip:
```bash
pip install fastapi uvicorn pydantic python-decouple loguru
```

4. **Configure environment variables:**

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` to customize your settings (optional, defaults are provided):
```env
API_TITLE=Randomizer API
API_VERSION=1.0.0
ALLOWED_ORIGINS=http://localhost:3000,https://example.com
ITEMS_PER_PAGE=21
LOG_LEVEL=INFO
MAX_ITEM_NAME_LENGTH=100
```

## Usage

### Starting the Server

Using Makefile (recommended):
```bash
make run
```

Or directly with uvicorn:
```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Other Make Commands

```bash
make lint          # Run code linter (ruff)
```

### Interactive API Documentation

Once the server is running, access the documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Testing with REST Client

The project includes a comprehensive `client.http` file for testing all endpoints using the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) VSCode extension.

1. Install the REST Client extension in VSCode
2. Open `client.http`
3. Click "Send Request" above any endpoint
4. View responses in the side panel

The file includes 39+ test cases covering:
- All CRUD operations
- Error scenarios
- Validation testing
- Pagination examples

## API Endpoints

### Random Playground

#### `GET /`
Welcome endpoint that returns a greeting message.

**Response:**
```json
{
  "message": "Welcome to the Randomizer API"
}
```

#### `GET /random/{max_value}`
Generate a random number between 1 and the specified maximum value.

**Parameters:**
- `max_value` (path parameter): Maximum value for random generation

**Example:**
```bash
curl http://localhost:8000/random/100
```

**Response:**
```json
{
  "max": 100,
  "random_number": 42
}
```

#### `GET /random-between`
Generate a random number within a specific range.

**Query Parameters:**
- `min_value` (optional, default=1): Minimum value (1-1000)
- `max_value` (optional, default=99): Maximum value (1-1000)

**Example:**
```bash
curl "http://localhost:8000/random-between?min_value=10&max_value=50"
```

**Response:**
```json
{
  "min": 10,
  "max": 50,
  "random_number": 27
}
```

### Random Items Management

#### `POST /items`
Add a new item to the list.

**Request Body:**
```json
{
  "name": "Apple"
}
```

**Response:**
```json
{
  "message": "Item added successfully",
  "item": "Apple"
}
```

**Validation:**
- Name must be 1-100 characters
- Duplicate names are not allowed

#### `GET /items`
Retrieve paginated items with both original and randomized ordering.

**Query Parameters:**
- `page` (optional, default=1): Page number (must be >= 1)

**Example:**
```bash
curl "http://localhost:8000/items?page=1"
```

**Response:**
```json
{
  "original_order": ["Apple", "Banana", "Cherry"],
  "randomized_order": ["Cherry", "Apple", "Banana"],
  "count": 3,
  "page": 1,
  "per_page": 21,
  "total_pages": 1
}
```

#### `PUT /items/{update_item_name}`
Update an existing item's name.

**Parameters:**
- `update_item_name` (path parameter): Current item name

**Request Body:**
```json
{
  "name": "Orange"
}
```

**Response:**
```json
{
  "message": "Item updated successfully",
  "old_item": "Apple",
  "new_item": "Orange"
}
```

#### `DELETE /items/{item}`
Delete an item from the list.

**Parameters:**
- `item` (path parameter): Item name to delete

**Response:**
```json
{
  "message": "Item deleted successfully",
  "deleted_item": "Apple",
  "remaining_items_count": 2
}
```

## Logging

The application uses **Loguru** for structured logging with:

- **Console Output**: Colored, formatted logs in the terminal
- **File Output**: Persistent logs in `logs/app.log`
  - Rotation: 500 MB per file
  - Retention: 10 days
  - Format: JSON-compatible structured logs

**Log Levels**: Configurable via `LOG_LEVEL` in `.env` (DEBUG, INFO, WARNING, ERROR)

Example log entry:
```
2025-11-06 10:01:38 | INFO     | app.routers.items:add_item:26 - Attempting to add item: apple
2025-11-06 10:01:38 | SUCCESS  | app.routers.items:add_item:33 - Item added successfully: apple
```

## CORS Configuration

CORS is configured via environment variables in `.env`:

```env
ALLOWED_ORIGINS=http://localhost:3000,https://example.com
```

Default settings:
- **Origins**: Comma-separated list from environment
- **Credentials**: Enabled
- **Methods**: GET, POST, PUT, DELETE
- **Headers**: All (`*`)

Middleware configuration: `app/main.py:24-32`

## Error Handling

The API uses standard HTTP status codes:
- `200 OK`: Successful request
- `400 Bad Request`: Invalid input or duplicate item
- `404 Not Found`: Item not found
- `409 Conflict`: Item name already exists
- `422 Unprocessable Entity`: Validation errors

Example error response:
```json
{
  "detail": "Item not found"
}
```

## Project Structure

```
fastapi-python-web-apis/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Environment-based configuration
│   ├── database.py          # SQLite database setup
│   ├── logger.py            # Loguru logging configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py          # Pydantic models for items
│   └── routers/
│       ├── __init__.py
│       ├── items.py         # Item management endpoints
│       └── random.py        # Random number endpoints
├── logs/
│   └── app.log              # Application logs (auto-generated)
├── .env                     # Environment variables (create from .env.example)
├── .env.example             # Example environment configuration
├── .gitignore
├── client.http              # REST Client test suite
├── Makefile                 # Build commands (run, lint)
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

## Database

The application uses **SQLite in-memory database** for development:

- **Type**: In-memory (`:memory:`)
- **Schema**: Auto-initialized on startup
- **Context Manager**: Safe transaction handling with `get_cursor()`
- **Features**:
  - Unique constraints on item names
  - Automatic timestamps
  - Transaction rollback on errors

**Note**: As an in-memory database, all data is lost when the application stops. For production, consider migrating to PostgreSQL or MySQL with persistent storage.

### Database Schema

```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Configuration

All configuration is managed through environment variables using `python-decouple`:

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `API_TITLE` | string | `Randomizer API` | API title in docs |
| `API_DESCRIPTION` | string | `Shuffle lists...` | API description |
| `API_VERSION` | string | `1.0.0` | API version |
| `ALLOWED_ORIGINS` | CSV | `http://localhost:3000,...` | CORS allowed origins |
| `ITEMS_PER_PAGE` | int | `21` | Items per page for pagination |
| `MAX_ITEM_NAME_LENGTH` | int | `100` | Maximum item name length |
| `LOG_LEVEL` | string | `INFO` | Logging level |

Configuration file: `app/config.py`

## Development

### Code Quality

The project uses **Ruff** for linting:

```bash
make lint              # Check code style
ruff check .           # Alternative command
ruff check . --fix     # Auto-fix issues
```

### Adding New Endpoints

1. **Create/Update Router**: Add endpoint in appropriate router (`app/routers/`)
2. **Define Models**: Create Pydantic models in `app/models/`
3. **Add Logging**: Use `logger.info()`, `logger.warning()`, etc.
4. **Database Operations**: Use `get_cursor()` context manager
5. **Error Handling**: Raise `HTTPException` with appropriate status codes
6. **Documentation**: Add docstrings and tag endpoints
7. **Testing**: Add test cases to `client.http`

### Best Practices

- ✅ Use type hints for all function parameters and returns
- ✅ Validate input with Pydantic models
- ✅ Log important operations and errors
- ✅ Use database context managers for safe transactions
- ✅ Return appropriate HTTP status codes
- ✅ Keep routers focused and organized
- ✅ Use environment variables for configuration

## Quick Reference

### Common Operations

```bash
# Start the server
make run

# Run linter
make lint

# View logs
tail -f logs/app.log

# Test all endpoints
# Open client.http in VSCode with REST Client extension

# Check API documentation
# Open http://localhost:8000/docs in browser
```

### Example Requests

```bash
# Add an item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple"}'

# Get items (with pagination)
curl http://localhost:8000/items?page=1

# Generate random number
curl http://localhost:8000/random/100

# Generate random in range
curl "http://localhost:8000/random-between?min_value=1&max_value=100"
```

## Recent Improvements

### Version 1.0.0
- ✅ Modular architecture with separation of concerns
- ✅ SQLite in-memory database replacing simple list
- ✅ Environment-based configuration with python-decouple
- ✅ Structured logging with Loguru (console + file)
- ✅ Pagination support (21 items per page)
- ✅ Comprehensive test suite in `client.http`
- ✅ Input validation improvements
- ✅ Database context managers for safe transactions
- ✅ Code quality improvements with Ruff linting
- ✅ Enhanced error handling and HTTP status codes
- ✅ Professional project structure

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built with FastAPI and Python

**Repository**: [github.com/carvalhocaio/fastapi-python-web-apis](https://github.com/carvalhocaio/fastapi-python-web-apis)

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://docs.pydantic.dev/) - Data validation using Python type annotations
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server
- [python-decouple](https://github.com/HBNetwork/python-decouple) - Strict separation of settings from code
- [Loguru](https://github.com/Delgan/loguru) - Python logging made simple
- [SQLite](https://www.sqlite.org/) - Self-contained, serverless database engine
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!
