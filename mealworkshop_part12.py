# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: MealWorkshop
import json, os

def load_recipe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'name' in data:
            return data
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Warning: Skipping malformed or missing file {path}: {type(e).__name__}")
    return None

def load_all_recipes(folder):
    recipes = []
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            recipe = load_recipe(os.path.join(folder, filename))
            if recipe:
                recipes.append(recipe)
    return recipes
