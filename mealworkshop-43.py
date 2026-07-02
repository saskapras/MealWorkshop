# === Stage 43: Add CSV import for the primary record type ===
# Project: MealWorkshop
import csv, json
from pathlib import Path

def load_csv_records(file_path: str, record_type: str) -> list[dict]:
    """Import records from a CSV file into the internal JSON structure."""
    data = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {
                "id": int(row.get("id", 0)),
                "type": record_type,
                **{k.strip(): v.strip() if isinstance(v, str) else v for k, v in row.items()}
            }
            data.append(record)
    return data

def merge_csv_to_project(csv_file: str, project_path: Path = None):
    """Load CSV and append records to the main project JSON file."""
    if project_path is None:
        project_path = Path("mealworkshop.json")
    
    existing_data = []
    with open(project_path, 'r', encoding='utf-8') as f:
        try:
            existing_data = json.load(f)
        except FileNotFoundError:
            pass
    
    new_records = load_csv_records(csv_file, "recipe")
    all_records = existing_data.get("recipes", []) + new_records
    
    # Sort by ID and remove duplicates based on id+name
    seen_ids = set()
    unique_records = []
    for r in sorted(all_records, key=lambda x: (x["id"], x.get("name", ""))):
        if r["id"] not in seen_ids:
            seen_ids.add(r["id"])
            unique_records.append(r)
    
    merged_project = {"recipes": unique_records}
    
    with open(project_path, 'w', encoding='utf-8') as f:
        json.dump(merged_project, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    merge_csv_to_project("ingredients.csv")
