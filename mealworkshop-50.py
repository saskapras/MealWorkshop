# === Stage 50: Add unit tests for import and export behavior ===
# Project: MealWorkshop
import json, os, tempfile
from pathlib import Path
from mealworkshop.core import Recipe, Menu, ShoppingList, MealPlan

def test_import_export():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup minimal data
        r = Recipe(name="Pasta", ingredients=["flour", "water"], steps=["mix"])
        m = Menu(name="Lunch")
        plan = MealPlan(days=1)
        
        # Export to JSON
        json_path = Path(tmpdir) / "data.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(plan.to_dict(), f, indent=2)
            
        # Verify round-trip integrity
        loaded_plan = MealPlan.from_json(json_path.read_text(encoding='utf-8'))
        
        assert len(loaded_plan.days) == 1
        assert loaded_plan.days[0].name == "Day 1"
        assert loaded_plan.days[0].menu.name == "Lunch"
        assert loaded_plan.days[0].menu.recipes[0].name == "Pasta"
