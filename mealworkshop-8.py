# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: MealWorkshop
from typing import Optional, List, Callable
import re

def filter_meals(
    meals: List[dict],
    status_filter: Optional[str] = None,
    category_filter: Optional[str] = None,
    owner_filter: Optional[str] = None,
    tag_filters: Optional[List[str]] = None
) -> List[dict]:
    """Filter meal entries by optional criteria."""
    if not meals: return []
    
    filtered = meals
    
    # Normalize filters to lowercase for case-insensitive matching
    status_map = {"planned": "planned", "cooking": "cooking", "done": "done"}
    category_map = {"breakfast": "breakfast", "lunch": "lunch", "dinner": "dinner", "snack": "snack"}
    
    if status_filter:
        normalized_status = status_map.get(status_filter.lower(), "")
        filtered = [m for m in filtered if not normalized_status or m.get("status") == normalized_status]
        
    if category_filter:
        normalized_cat = category_map.get(category_filter.lower(), "")
        filtered = [m for m in filtered if not normalized_cat or m.get("category") == normalized_cat]
        
    if owner_filter:
        # Supports partial matching (e.g., "joh" matches "john_doe")
        pattern = re.compile(owner_filter, re.IGNORECASE)
        filtered = [m for m in filtered if pattern.search(m.get("owner", ""))]
        
    if tag_filters:
        query_tags = set(t.lower() for t in tag_filters)
        def has_any_tag(meal):
            meal_tags = {t.strip().lower(): True for t in meal.get("tags", [])}
            return bool(query_tags & meal_tags.keys())
        filtered = [m for m in filtered if not tag_filters or has_any_tag(m)]
        
    return filtered
