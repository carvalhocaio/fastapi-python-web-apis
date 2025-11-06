"""Application configuration"""

from decouple import Csv, config

# API Metadata
API_TITLE = config("API_TITLE", default="Randomizer API")
API_DESCRIPTION = config(
	"API_DESCRIPTION",
	default="Shuffle lists, pick random items, and generate random numbers.",
)
API_VERSION = config("API_VERSION", default="1.0.0")

# CORS Configuration
ALLOWED_ORIGINS = config(
	"ALLOWED_ORIGINS",
	cast=Csv(),
	default="http://localhost:3000,https://example.com",
)

# Pagination
ITEMS_PER_PAGE = config("ITEMS_PER_PAGE", cast=int, default=21)

# Item Configuration
MAX_ITEM_NAME_LENGTH = config("MAX_ITEM_NAME_LENGTH", cast=int, default=100)

# Logging Configuration
LOG_LEVEL = config("LOG_LEVEL", default="INFO")

# Tags Metadata
TAGS_METADATA = [
	{
		"name": "Random Playground",
		"description": "Generate random numbers",
	},
	{
		"name": "Random Items Management",
		"description": "Create, shuffle, read, update and delete items",
	},
]
