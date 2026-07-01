# === Stage 41: Add plain text import for a simple line-based format ===
# Project: MealWorkshop
from typing import List, Dict, Optional
import json
import csv
import os

class MealImporter:
    """Handles importing recipes from simple CSV/text files."""
    
    def __init__(self):
        self.recipes: List[Dict] = []
        
    def parse_csv_recipe(self, file_path: str) -> Dict:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                recipe = {
                    "name": row.get("name", ""),
                    "ingredients": [ing.strip() for ing in row.get("ingredients", "").split(";") if ing.strip()],
                    "cooking_time": int(row.get("time_min", 0)),
                    "calories": int(row.get("kcal", 0))
                }
                self.recipes.append(recipe)
        return recipe
    
    def parse_text_recipe(self, file_path: str) -> Dict:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        name_line = next((l for l in lines if "name:" in l.lower()), "")
        time_line = next((l for l in lines if "time:" in l.lower()), "")
        kcal_line = next((l for l in lines if "kcal:" in l.lower()), "")
        
        ingredients_block = []
        current_ing = ""
        for line in lines:
            if line.startswith("ingredients:") or line.startswith("-"):
                continue
            elif line and not line.startswith("#") and not line.startswith("name:") and not line.startswith("time:") and not line.startswith("kcal:"):
                current_ing += " " + line.strip()
            else:
                if current_ing:
                    ingredients_block.append(current_ing)
                current_ing = ""
        
        return {
            "name": name_line.split(":")[1].strip() if ":" in name_line else "",
            "ingredients": ingredients_block,
            "cooking_time": int(time_line.split(":")[1].strip()) if time_line and ":" in time_line else 0,
            "calories": int(kcal_line.split(":")[1].strip()) if kcal_line and ":" in kcal_line else 0
        }

def load_all_recipes(directory: str) -> List[Dict]:
    importer = MealImporter()
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            importer.parse_csv_recipe(os.path.join(directory, filename))
        elif filename.endswith(".txt"):
            importer.parse_text_recipe(os.path.join(directory, filename))
    return importer.recipes

if __name__ == "__main__":
    recipes = load_all_recipes("recipes")
    for r in recipes:
        print(f"{r['name']}: {len(r['ingredients'])} ingredients, {r['cooking_time']} min")
