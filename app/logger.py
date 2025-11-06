"""Logging configuration using loguru"""

import sys

from loguru import logger

from app.config import LOG_LEVEL


def setup_logger() -> None:
	"""Configure loguru logger"""
	# Remove default handler
	logger.remove()

	# Add custom handler with formatting
	logger.add(
		sys.stdout,
		level=LOG_LEVEL,
		format=(
			"<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
			"<level>{level: <8}</level> | "
			"<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
			"<cyan>{line}</cyan> - <level>{message}</level>"
		),
		colorize=True,
	)

	# Add file handler for persistent logs
	logger.add(
		"logs/app.log",
		rotation="500 MB",
		retention="10 days",
		level=LOG_LEVEL,
		format=(
			"{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | "
			"{name}:{function}:{line} - {message}"
		),
	)


# Initialize logger
setup_logger()
