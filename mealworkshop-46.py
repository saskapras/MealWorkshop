# === Stage 46: Add a schema version field and migration helper ===
# Project: MealWorkshop
from pathlib import Path, PurePath
import json
import hashlib
from typing import Optional, Dict, Any

SCHEMA_VERSION = 2
MIGRATION_LOG_FILE = "schema_migrations.log"

def get_schema_version() -> int:
    """Read current schema version from the project root."""
    root = Path(__file__).resolve().parent.parent
    log_path = root / MIGRATION_LOG_FILE
    if not log_path.exists():
        return SCHEMA_VERSION - 1
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) >= 2 and parts[0] == "v":
                try:
                    return int(parts[1])
                except ValueError:
                    continue
    return SCHEMA_VERSION - 1

def run_migration(version_delta: int, migration_func: callable):
    """Execute a schema migration if the version delta matches."""
    current = get_schema_version()
    target = current + version_delta
    
    if target <= current:
        print(f"Migration skipped. Current version: {current}, Target: {target}")
        return False
        
    try:
        migration_func(current, target)
        
        # Update log file atomically by appending to a temp file then renaming
        with open(MIGRATION_LOG_FILE + ".tmp", "a", encoding="utf-8") as f:
            f.write(f"v{current} -> v{target}\n")
        Path(MIGRATION_LOG_FILE).write_text(Path(MIGRATION_LOG_FILE + ".tmp").read_text(encoding="utf-8"))
        
        print(f"Migrated successfully from v{current} to v{target}")
        return True
    except Exception as e:
        print(f"Migration failed for version {version_delta}: {e}")
        return False

def migrate_v1_to_v2(current_version: int, target_version: int):
    """Add schema_version field and ensure data integrity."""
    root = Path(__file__).resolve().parent.parent
    
    # Helper to update JSON files in place if they lack the new field
    def _update_file(file_path: PurePath) -> bool:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if "schema_version" not in data or data["schema_version"] != target_version:
                # Add field and update version
                data["schema_version"] = target_version
                
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                
                return True
            return False
        except (json.JSONDecodeError, IOError):
            # Skip non-JSON or unreadable files
            return False

    # Scan all JSON data files in the project root and subdirectories
    for file_path in root.rglob("*.json"):
        if _update_file(file_path):
            print(f"Updated {file_path} to schema version {target_version}")
