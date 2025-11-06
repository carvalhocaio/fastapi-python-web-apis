"""Items management endpoints"""

import math
import random
import sqlite3

from fastapi import APIRouter, HTTPException, Query, status
from loguru import logger

from app.config import ITEMS_PER_PAGE
from app.database import get_cursor
from app.models import (
	Item,
	ItemDeleteResponse,
	ItemListResponse,
	ItemResponse,
	ItemUpdateResponse,
)

router = APIRouter(prefix="/items", tags=["Random Items Management"])


@router.post("", response_model=ItemResponse)
def add_item(item: Item):
	"""Add a new item to the database"""
	logger.info(f"Attempting to add item: {item.name}")

	try:
		with get_cursor() as cursor:
			cursor.execute(
				"INSERT INTO items (name) VALUES (?)", (item.name,)
			)
		logger.success(f"Item added successfully: {item.name}")
		return ItemResponse(message="Item added successfully", item=item.name)
	except sqlite3.IntegrityError:
		logger.warning(f"Item already exists: {item.name}")
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Item already exists",
		)


@router.get("", response_model=ItemListResponse)
def get_randomized_items(
	page: int = Query(default=1, ge=1, description="Page number"),
):
	"""Get paginated randomized items"""
	logger.info(f"Fetching randomized items for page {page}")

	with get_cursor() as cursor:
		# Get total count
		cursor.execute("SELECT COUNT(*) as total FROM items")
		total_count = cursor.fetchone()["total"]

		# Calculate pagination
		total_pages = math.ceil(total_count / ITEMS_PER_PAGE)
		offset = (page - 1) * ITEMS_PER_PAGE

		# Get all items for original order (limited to current page)
		cursor.execute(
			"SELECT name FROM items ORDER BY id LIMIT ? OFFSET ?",
			(ITEMS_PER_PAGE, offset),
		)
		items = [row["name"] for row in cursor.fetchall()]

	# Create randomized copy
	randomized = items.copy()
	random.shuffle(randomized)

	logger.info(
		f"Returning {len(items)} items "
		f"(page {page}/{total_pages}, total: {total_count})"
	)

	return ItemListResponse(
		original_order=items,
		randomized_order=randomized,
		count=len(items),
		page=page,
		per_page=ITEMS_PER_PAGE,
		total_pages=total_pages,
	)


@router.put("/{update_item_name}", response_model=ItemUpdateResponse)
def update_item(update_item_name: str, item: Item):
	"""Update an existing item"""
	logger.info(
		f"Attempting to update item: {update_item_name} -> {item.name}"
	)

	try:
		with get_cursor() as cursor:
			# Check if the old item exists
			cursor.execute(
				"SELECT name FROM items WHERE name = ?", (update_item_name,)
			)
			if not cursor.fetchone():
				logger.warning(f"Item not found: {update_item_name}")
				raise HTTPException(
					status_code=status.HTTP_404_NOT_FOUND,
					detail="Item not found",
				)

			# Update the item
			cursor.execute(
				"UPDATE items SET name = ? WHERE name = ?",
				(item.name, update_item_name),
			)

		logger.success(
			f"Item updated successfully: {update_item_name} -> {item.name}"
		)
		return ItemUpdateResponse(
			message="Item updated successfully",
			old_item=update_item_name,
			new_item=item.name,
		)
	except sqlite3.IntegrityError:
		logger.warning(f"An item with name '{item.name}' already exists")
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="An item with that name already exists",
		)


@router.delete("/{item}", response_model=ItemDeleteResponse)
def delete_item(item: str):
	"""Delete an item from the database"""
	logger.info(f"Attempting to delete item: {item}")

	with get_cursor() as cursor:
		# Check if item exists
		cursor.execute("SELECT name FROM items WHERE name = ?", (item,))
		if not cursor.fetchone():
			logger.warning(f"Item not found: {item}")
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail="Item not found",
			)

		# Delete the item
		cursor.execute("DELETE FROM items WHERE name = ?", (item,))

		# Get remaining count
		cursor.execute("SELECT COUNT(*) as total FROM items")
		remaining_count = cursor.fetchone()["total"]

	logger.success(f"Item deleted successfully: {item}")

	return ItemDeleteResponse(
		message="Item deleted successfully",
		deleted_item=item,
		remaining_items_count=remaining_count,
	)
