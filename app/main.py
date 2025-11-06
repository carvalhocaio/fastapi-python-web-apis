"""FastAPI application entry point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.config import (
	ALLOWED_ORIGINS,
	API_DESCRIPTION,
	API_TITLE,
	API_VERSION,
	TAGS_METADATA,
)
from app.logger import setup_logger  # noqa: F401
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


@app.on_event("startup")
async def startup_event():
	"""Log application startup"""
	logger.info(f"Starting {API_TITLE} v{API_VERSION}")
	logger.info(f"CORS enabled for origins: {ALLOWED_ORIGINS}")


@app.on_event("shutdown")
async def shutdown_event():
	"""Log application shutdown"""
	logger.info(f"Shutting down {API_TITLE}")
