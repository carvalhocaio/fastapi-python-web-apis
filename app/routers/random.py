"""Random number generation endpoints"""

import random
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

router = APIRouter(prefix="", tags=["Random Playground"])


@router.get("/")
async def home():
	return {"message": "Welcome to the Randomizer API"}


@router.get("/random/{max_value}")
async def get_random_number(max_value: int):
	return {"max": max_value, "random_number": random.randint(1, max_value)}


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
	if min_value > max_value:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="min_value can't be greater than max_value",
		)

	return {
		"min": min_value,
		"max": max_value,
		"random_number": random.randint(min_value, max_value),
	}
