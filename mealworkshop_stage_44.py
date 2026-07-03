# === Stage 44: Add backup creation for the data file ===
# Project: MealWorkshop
import json, os, datetime

def backup_data(data_file: str) -> None:
    if not os.path.exists(data_file):
        return
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{data_file}.backup_{timestamp}"
    
    try:
        with open(data_file, "r", encoding="utf-8") as src:
            data = json.load(src)
        
        with open(backup_path, "w", encoding="utf-8") as dst:
            json.dump(data, dst, indent=2, ensure_ascii=False)
        
    except Exception as e:
        print(f"Backup failed: {e}")
