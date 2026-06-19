# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: MealWorkshop
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str
    cost_per_unit: float = 0.0
    category: str = "misc"

@dataclass
class Recipe:
    title: str
    description: str
    ingredients: List[Ingredient] = field(default_factory=list)
    prep_time_minutes: int = 0
    nutrition_notes: Optional[str] = None

@dataclass
class MenuDay:
    date: date
    breakfast: Optional[Recipe] = None
    lunch: Optional[Recipe] = None
    dinner: Optional[Recipe] = None
    notes: str = ""

@dataclass
class ShoppingList:
    items: List[Ingredient] = field(default_factory=list)
    total_cost: float = 0.0
    date_created: date = field(default_factory=date)
