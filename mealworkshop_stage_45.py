# === Stage 45: Add restore from backup with validation ===
# Project: MealWorkshop
import json, os, hashlib
from pathlib import Path

def validate_recipe(data: dict) -> bool:
    required = {"name", "ingredients", "steps"}
    return all(k in data for k in required) and isinstance(data["ingredients"], list)

def restore_backup(backup_path: str, target_dir: str):
    if not os.path.exists(backup_path):
        print(f"Backup file '{backup_path}' not found.")
        return False
    
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        
        if not isinstance(backup_data, list):
            print("Invalid backup structure: expected a list of recipes.")
            return False
            
        valid_count = 0
        for i, recipe in enumerate(backup_data):
            if validate_recipe(recipe):
                target_file = os.path.join(target_dir, f"recipe_{i}.json")
                with open(target_file, 'w', encoding='utf-8') as out:
                    json.dump(recipe, out, indent=2)
                valid_count += 1
        
        print(f"Restored {valid_count} valid recipes from backup.")
        return True
    except json.JSONDecodeError as e:
        print(f"JSON decode error during restore: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during restore: {e}")
        return False
