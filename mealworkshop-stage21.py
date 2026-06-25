# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: MealWorkshop
from datetime import datetime, timedelta
import json
from pathlib import Path

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 365

def archive_old_records(data_dir: str):
    data_path = Path(data_dir)
    if not data_path.exists(): return
    
    today = datetime.now()
    cutoff_date = (today - timedelta(days=RETENTION_DAYS)).date()
    
    for file in data_path.glob("*.json"):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                records = json.load(f)
            
            if not isinstance(records, list): continue
            
            active_records = []
            archived_items = []
            
            for record in records:
                created_date_str = record.get('created_at') or record.get('date')
                if not created_date_str: continue
                
                try:
                    created_date = datetime.strptime(created_date_str, '%Y-%m-%d').date()
                    
                    if created_date < cutoff_date:
                        archived_items.append(record)
                    else:
                        active_records.append(record)
                        
                except ValueError:
                    active_records.append(record)
            
            if archived_items:
                archive_path = data_path.parent / ARCHIVE_DIR / f"{file.stem}_old.json"
                with open(archive_path, 'w', encoding='utf-8') as af:
                    json.dump({
                        "archived_at": datetime.now().isoformat(),
                        "source_file": file.name,
                        "records": archived_items
                    }, af, indent=2)
                
                # Remove old records from main file if empty or update in place
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(active_records, f, indent=2)

        except (json.JSONDecodeError, IOError):
            continue
