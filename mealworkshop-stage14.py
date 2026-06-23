# === Stage 14: Add file load support with fallback demo data ===
# Project: MealWorkshop
def load_data(source=None):
    if source:
        try:
            with open(source, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            pass
    demo = {
        "recipes": [{"id": 1, "name": "Pasta", "ingredients": ["Flour", "Eggs"], "cost": 2.5}],
        "menus": [{"day": "Monday", "recipe_id": 1}],
        "shopping_list": []
    }
    return demo
