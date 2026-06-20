# === Stage 4: Implement create operations for the primary records ===
# Project: MealWorkshop
from typing import Optional, List
import json
from datetime import date

class Recipe:
    def __init__(self, name: str, ingredients: dict, prep_time_min: int):
        self.name = name
        self.ingredients = ingredients  # {item_name: quantity}
        self.prep_time_min = prep_time_min

    def to_dict(self) -> dict:
        return {"name": self.name, "ingredients": self.ingredients, "prep_time_min": self.prep_time_min}

class Menu:
    def __init__(self, day: date, meals: List[Recipe]):
        self.day = day
        self.meals = meals  # [breakfast, lunch, dinner]

    def to_dict(self) -> dict:
        return {"day": str(self.day), "meals": [m.to_dict() for m in self.meals]}

class ShoppingList:
    def __init__(self):
        self.items: List[dict] = []  # [{"item": ..., "quantity": ...}]

    def add_item(self, item_name: str, quantity: float) -> None:
        existing = next((i for i in self.items if i["item"] == item_name), None)
        if existing:
            existing["quantity"] += quantity
        else:
            self.items.append({"item": item_name, "quantity": quantity})

    def to_dict(self) -> dict:
        return {"items": sorted(self.items, key=lambda x: x["item"])}
