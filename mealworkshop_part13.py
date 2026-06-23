# === Stage 13: Add file save support using a configurable path ===
# Project: MealWorkshop
import os
from pathlib import Path

class ConfigurablePath:
    def __init__(self, base_dir=None):
        self.base_path = Path(base_dir) if base_dir else Path.cwd() / "MealWorkshop"
        self.data_files = {
            "recipes": self.base_path / "data" / "recipes.json",
            "menus": self.base_path / "data" / "menus.json",
            "shopping": self.base_path / "data" / "shopping.json",
            "nutrition": self.base_path / "data" / "nutrition.txt"
        }

    def ensure_dirs(self):
        for path in self.data_files.values():
            path.parent.mkdir(parents=True, exist_ok=True)

    def save_recipe(self, recipe_id: str, data: dict):
        with open(self.data_files["recipes"], 'w', encoding='utf-8') as f:
            json.dump({recipe_id: data}, f, indent=2, ensure_ascii=False)

    def load_all_data(self) -> dict:
        self.ensure_dirs()
        result = {}
        for key in ["recipes", "menus", "shopping"]:
            path = self.data_files[key]
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    result.update(data)
        return result

    def append_nutrition(self, note: str):
        with open(self.data_files["nutrition"], 'a', encoding='utf-8') as f:
            f.write(note + "\n")
