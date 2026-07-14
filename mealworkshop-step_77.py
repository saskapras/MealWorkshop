# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: MealWorkshop
from typing import List, Optional, Dict


def get_ingredients_by_category(
    ingredients: List[Dict[str, str]], category: str
) -> List[Dict[str, str]]:
    """Return all ingredients belonging to a given category."""
    return [ing for ing in ingredients if ing.get("category") == category]
