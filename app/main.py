"""FastAPI application entry point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import (
	ALLOWED_ORIGINS,
	API_DESCRIPTION,
	API_TITLE,
	API_VERSION,
	TAGS_METADATA,
)
from app.routers import items, random

# Initialize FastAPI app
app = FastAPI(
	title=API_TITLE,
	description=API_DESCRIPTION,
	version=API_VERSION,
	openapi_tags=TAGS_METADATA,
)

# Configure CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=ALLOWED_ORIGINS,
	allow_credentials=True,
	allow_methods=["GET", "POST", "PUT", "DELETE"],
	allow_headers=["*"],
)

# Include routers
app.include_router(random.router)
app.include_router(items.router)
