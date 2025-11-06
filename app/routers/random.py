"""Random number generation endpoints"""

import random
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status
from loguru import logger

router = APIRouter(prefix="", tags=["Random Playground"])


@router.get("/")
def home():
	"""Welcome endpoint"""
	logger.info("Home endpoint accessed")
	return {"message": "Welcome to the Randomizer API"}


@router.get("/random/{max_value}")
def get_random_number(max_value: int):
	"""Generate a random number between 1 and max_value"""
	logger.info(f"Generating random number with max_value: {max_value}")

	if max_value < 1:
		logger.warning(f"Invalid max_value provided: {max_value}")
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="max_value must be at least 1",
		)

	result = random.randint(1, max_value)
	logger.debug(f"Generated random number: {result}")
	return {"max": max_value, "random_number": result}


@router.get("/random-between")
def get_random_number_between(
	min_value: Annotated[
		int,
		Query(
			title="Minimum Value",
			description="The minimum random number",
			ge=1,
			le=1000,
		),
	] = 1,
	max_value: Annotated[
		int,
		Query(
			title="Maximum Value",
			description="The maximum random number",
			ge=1,
			le=1000,
		),
	] = 99,
):
	"""Generate a random number between min_value and max_value"""
	logger.info(
		f"Generating random number between {min_value} and {max_value}"
	)

	if min_value > max_value:
		logger.warning(
			f"Invalid range: min_value ({min_value}) > max_value ({max_value})"
		)
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="min_value can't be greater than max_value",
		)

	result = random.randint(min_value, max_value)
	logger.debug(f"Generated random number: {result}")
	return {
		"min": min_value,
		"max": max_value,
		"random_number": result,
	}
