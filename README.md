# Randomizer API

A FastAPI-based REST API for generating random numbers and managing
randomizable item lists. This project demonstrates modern Python API
development with FastAPI, including proper data validation, CORS
configuration, and comprehensive API documentation.

## Features

- **Random Number Generation**
  - Generate random numbers up to a maximum value
  - Generate random numbers within a specific range (min-max)
  - Input validation and error handling

- **Item Management**
  - Create items with validation
  - List items with randomized ordering
  - Update existing items
  - Delete items
  - Automatic duplicate detection

- **Additional Features**
  - Interactive API documentation (Swagger UI)
  - CORS middleware for cross-origin requests
  - Pydantic models for request/response validation
  - Proper HTTP status codes and error messages
  - Tagged endpoints for organized documentation

## Requirements

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/carvalhocaio/fastapi-python-web-apis
cd fastapi-python-web-apis
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

## Usage

### Starting the Server

Run the development server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

Once the server is running, access the interactive documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

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
Retrieve all items with both original and randomized ordering.

**Response:**
```json
{
  "original_order": ["Apple", "Banana", "Cherry"],
  "randomized_order": ["Cherry", "Apple", "Banana"],
  "count": 3
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

## CORS Configuration

The API is configured with CORS middleware allowing:
- Origins: `http://localhost:3000`, `https://example.com`
- Credentials: Enabled
- Methods: GET, POST, PUT, DELETE
- Headers: All

To modify CORS settings, edit the middleware configuration in `main.py:25-31`.

## Error Handling

The API uses standard HTTP status codes:
- `200 OK`: Successful request
- `400 Bad Request`: Invalid input or duplicate item
- `404 Not Found`: Item not found
- `409 Conflict`: Item name already exists

Example error response:
```json
{
  "detail": "Item not found"
}
```

## Project Structure

```
fastapi-python-web-apis/
├── main.py          # Main application file with all endpoints
└── README.md        # This file
```

## Development

### Adding New Endpoints

1. Define Pydantic models for request/response validation
2. Create the endpoint function with appropriate decorators
3. Add proper tags for documentation organization
4. Implement error handling with HTTPException

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

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://docs.pydantic.dev/) - Data validation using Python type annotations
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server
