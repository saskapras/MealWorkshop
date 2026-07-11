# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: MealWorkshop
python
import json


def reset_demo_data(db):
    """Clear all tables and re-seed demo data for manual testing."""
    db.exec("DELETE FROM meal_plans")
    db.exec("DELETE FROM menu_items")
    db.exec("DELETE FROM shopping_lists")
    db.exec("DELETE FROM items")
    db.exec("DELETE FROM recipe_ingredients")
    db.exec("DELETE FROM recipes")

    demo_recipes = [
        {"name": "Salad", "prep_min": 5, "cook_min": 0, "servings": 2},
        {"name": "Pasta", "prep_min": 15, "cook_min": 20, "servings": 4},
    ]
    for r in demo_recipes:
        db.exec("INSERT INTO recipes (name, prep_min, cook_min, servings) VALUES (:n, :p, :c, :s)", **r)

    demo_items = [
        {"name": "Lettuce", "unit": "head", "price": 2.0},
        {"name": "Tomato", "unit": "each", "price": 1.5},
        {"name": "Pasta", "unit": "box", "price": 3.0},
    ]
    for item in demo_items:
        db.exec("INSERT INTO items (name, unit, price) VALUES (:n, :u, :p)", **item)

    demo_menus = [
        {"date": "2026-12-01", "recipe_id": 1},
        {"date": "2026-12-02", "recipe_id": 2},
    ]
    for m in demo_menus:
        db.exec("INSERT INTO menu_items (date, recipe_id) VALUES (:d, :r)", **m)

    print("Demo data reset complete.")


if __name__ == "__main__":
    from sqlite3 import connect
    db = connect("mealworkshop.db")
    reset_demo_data(db)
    db.close()
python
