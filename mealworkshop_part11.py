# === Stage 11: Add JSON export for the current application state ===
# Project: MealWorkshop
import json, os
from pathlib import Path

def export_state(base_path: str = ".") -> dict | None:
    recipes = []
    menus = []
    shopping_lists = {}
    
    for f in Path(base_path).glob("recipes/*.json"):
        with open(f) as fp: data = json.load(fp); recipes.append(data)
    for f in Path(base_path).glob("menus/*.json"):
        with open(f) as fp: menus.append(json.load(fp))
    
    for f in Path(base_path).glob("shopping_lists/*.txt"):
        name = f.stem; lines = [l.strip() for l in f.read_text().splitlines() if l.strip()]
        shopping_lists[name] = lines
    
    state = {"recipes": recipes, "menus": menus, "shopping_lists": shopping_lists}
    
    try:
        with open(Path(base_path) / "state_export.json", "w") as fp: json.dump(state, fp, indent=2)
        return state
    except Exception: return None
