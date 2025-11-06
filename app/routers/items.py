"""Items management endpoints"""

import random

from fastapi import APIRouter, HTTPException, status

from app.database import items_db
from app.models import (
	Item,
	ItemDeleteResponse,
	ItemListResponse,
	ItemResponse,
	ItemUpdateResponse,
)

router = APIRouter(prefix="/items", tags=["Random Items Management"])


@router.post(
	"", response_model=ItemResponse, tags=["Random Items Management"]
)
def add_item(item: Item):
	if item.name in items_db:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Item already exists",
		)

	items_db.append(item.name)
	return ItemResponse(message="Item added successfully", item=item.name)


@router.get(
	"", response_model=ItemListResponse, tags=["Random Items Management"]
)
def get_randomized_items():
	randomized = items_db.copy()
	random.shuffle(randomized)
	return ItemListResponse(
		original_order=items_db,
		randomized_order=randomized,
		count=len(items_db),
	)


@router.put(
	"/{update_item_name}",
	response_model=ItemUpdateResponse,
	tags=["Random Items Management"],
)
def update_item(update_item_name: str, item: Item):
	if update_item_name not in items_db:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
		)

	if item.name in items_db:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="An item with that name already exists",
		)

	index = items_db.index(update_item_name)
	items_db[index] = item.name

	return ItemUpdateResponse(
		message="Item updated successfully",
		old_item=update_item_name,
		new_item=item.name,
	)


@router.delete(
	"/{items}",
	response_model=ItemDeleteResponse,
	tags=["Random Items Management"],
)
def delete_item(item: str):
	if item not in items_db:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
		)

	items_db.remove(item)

	return ItemDeleteResponse(
		message="Item deleted successfully",
		deleted_item=item,
		remaining_items_count=len(items_db),
	)
