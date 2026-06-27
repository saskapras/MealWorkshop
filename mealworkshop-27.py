# === Stage 27: Add monthly summary calculations ===
# Project: MealWorkshop
from datetime import date, timedelta
import json
from pathlib import Path

def calculate_monthly_summary(data_dir: str = "data") -> dict:
    """Aggregates recipes and menus for the current month to produce a summary report."""
    today = date.today()
    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    total_cost = 0.0
    total_calories = 0
    meal_count = 0
    unique_ingredients = set()

    recipes_path = Path(data_dir) / "recipes.json"
    menus_path = Path(data_dir) / "menus.json"

    if not recipes_path.exists():
        return {"error": "No recipes found"}
    
    with open(recipes_path, 'r', encoding='utf-8') as f:
        all_recipes = json.load(f)

    for recipe in all_recipes.values():
        prep_date_str = recipe.get("prepDate", "")
        if not prep_date_str:
            continue
        
        try:
            prep_date = date.fromisoformat(prep_date_str)
        except ValueError:
            continue
            
        if start_of_month <= prep_date < end_of_month:
            cost = float(recipe.get("totalCost", 0))
            calories = int(recipe.get("caloriesPerServing", 0)) * recipe.get("servings", 1)
            
            total_cost += cost
            total_calories += calories
            meal_count += 1
            
            for ingredient in recipe.get("ingredients", []):
                unique_ingredients.add(ingredient["name"])

    summary = {
        "month": f"{start_of_month.year}-{start_of_month.month:02d}",
        "totalCost": round(total_cost, 2),
        "totalCalories": total_calories,
        "mealCount": meal_count,
        "uniqueIngredients": len(unique_ingredients)
    }

    return summary
