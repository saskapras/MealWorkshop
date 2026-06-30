# === Stage 36: Add templates for quickly creating common records ===
# Project: MealWorkshop
from typing import Optional, Dict, List
import json
from pathlib import Path

class RecordTemplates:
    """Compact templates for quickly creating common MealWorkshop records."""
    
    @staticmethod
    def create_recipe(name: str, prep_time_min: int = 30, servings: int = 4) -> Dict[str, any]:
        return {
            "id": f"recipe_{name.lower().replace(' ', '_')}",
            "title": name,
            "prepTimeMinutes": prep_time_min,
            "servings": servings,
            "ingredients": [],
            "instructions": ["Step 1: Prepare ingredients.", "Step 2: Cook according to recipe."],
            "nutrition": {"calories": 0, "protein_g": 0},
            "tags": []
        }

    @staticmethod
    def create_menu(day: str = "Monday", meals: List[str] = None) -> Dict[str, any]:
        if meals is None:
            meals = ["Breakfast", "Lunch", "Dinner"]
        return {
            "id": f"menu_{day}",
            "date": day,
            "meals": [
                {"type": meal_type, "recipeId": "", "notes": ""} for meal_type in meals
            ],
            "totalCost": 0.0,
            "nutritionSummary": {}
        }

    @staticmethod
    def create_shopping_list(items: List[str] = None) -> Dict[str, any]:
        if items is None:
            items = ["Eggs", "Milk", "Bread"]
        return {
            "id": f"shopping_{len(items)}",
            "items": [{"name": item, "quantity": 1, "unit": "", "checked": False} for item in items],
            "totalEstimate": 0.0,
            "notes": ""
        }

    @staticmethod
    def create_nutrition_note(recipe_id: str, macros: Dict[str, float]) -> Dict[str, any]:
        return {
            "id": f"nutrition_{recipe_id}",
            "recipeId": recipe_id,
            "macros": {"calories": macros.get("calories", 0), "protein_g": macros.get("protein_g", 0)},
            "carbs_g": macros.get("carbs_g", 0),
            "fat_g": macros.get("fat_g", 0),
            "notes": ""
        }

    @staticmethod
    def save_all_to_file(templates: Dict[str, any], filename: str = "templates.json") -> None:
        """Save generated templates to a JSON file for reuse."""
        path = Path(filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({k: v for k, v in templates.items() if isinstance(v, dict)}, f, indent=2, ensure_ascii=False)
