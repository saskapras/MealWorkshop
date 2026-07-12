# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: MealWorkshop
def seed_demo_data(recipes, menus, shopping_lists):
    """Populate recipe/menulist/shoppinglist with deterministic sample data."""
    recipes.setdefault("chicken_stir_fry", {
        "name": "Chicken Stir Fry",
        "ingredients": [
            {"item": "chicken breast", "qty": 0.5, "unit": "kg"},
            {"item": "soy sauce", "qty": 2, "unit": "tbsp"},
            {"item": "broccoli florets", "qty": 1, "unit": "cup"},
        ],
    })
    recipes.setdefault("lentil_soup", {
        "name": "Lentil Soup",
        "ingredients": [
            {"item": "red lentils", "qty": 0.5, "unit": "kg"},
            {"item": "onion", "qty": 1, "unit": "whole"},
            {"item": "carrot", "qty": 2, "unit": "pieces"},
        ],
    })

    menus.setdefault("week1_monday", {
        "date": "2026-05-04",
        "meals": {"lunch": "chicken_stir_fry", "dinner": "lentil_soup"},
    })

    shopping_lists.setdefault("list_01", {
        "title": "Sample List",
        "items": [
            {"ingredient": "chicken breast", "qty": 2, "unit": "kg"},
            {"ingredient": "red lentils", "qty": 3, "unit": "kg"},
            {"ingredient": "onion", "qty": 5, "unit": "pieces"},
        ],
    })
