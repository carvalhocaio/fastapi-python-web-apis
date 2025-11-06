"""Pydantic models for items"""

from pydantic import BaseModel, Field


class Item(BaseModel):
	name: str = Field(
		min_length=1, max_length=100, description="The item name"
	)


class ItemResponse(BaseModel):
	message: str
	item: str


class ItemListResponse(BaseModel):
	original_order: list[str]
	randomized_order: list[str]
	count: int


class ItemUpdateResponse(BaseModel):
	message: str
	old_item: str
	new_item: str


class ItemDeleteResponse(BaseModel):
	message: str
	deleted_item: str
	remaining_items_count: int
