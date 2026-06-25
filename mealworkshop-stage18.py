# === Stage 18: Add an activity log with timestamps and action names ===
# Project: MealWorkshop
from datetime import datetime, timezone
import json
from pathlib import Path

LOG_FILE = "activity_log.json"

def log_action(action_name: str, details: dict | None = None) -> None:
    """Append a new entry to the activity log with timestamp and action name."""
    path = Path(LOG_FILE)
    if not path.exists():
        path.write_text("[]")
    
    data = json.loads(path.read_text())
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action_name,
        "details": details or {}
    }
    data.append(entry)
    # Keep log size manageable by limiting to last 100 entries
    if len(data) > 100:
        data = data[-100:]
    
    path.write_text(json.dumps(data, indent=2))

def get_log() -> list[dict]:
    """Return the current activity log as a list of dictionaries."""
    path = Path(LOG_FILE)
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
