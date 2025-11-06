"""Application configuration"""

# API Metadata
API_TITLE = "Randomizer API"
API_DESCRIPTION = (
	"Shuffle lists, pick random items, and generate random numbers."
)
API_VERSION = "1.0.0"

# CORS Configuration
ALLOWED_ORIGINS = [
	"http://localhost:3000",
	"https://example.com",
]

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
