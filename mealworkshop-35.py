# === Stage 35: Add active user switching and user-specific records ===
# Project: MealWorkshop
from typing import Optional, Dict, List
import json
from pathlib import Path

class UserContext:
    def __init__(self):
        self._current_user_id = None
        self._users_data: Dict[str, dict] = {}
    
    def load_users(self, file_path: Path) -> None:
        if not file_path.exists(): return
        with open(file_path) as f:
            raw = json.load(f)
            for u in raw.get("users", []):
                self._users_data[u["id"]] = u
    
    def switch_user(self, user_id: str) -> bool:
        if not self._current_user_id and self._users_data:
            self._current_user_id = list(self._users_data.keys())[0]
        if user_id in self._users_data:
            self._current_user_id = user_id
            return True
        return False
    
    def get_current_user(self) -> Optional[dict]:
        if not self._current_user_id:
            return None
        return self._users_data.get(self._current_user_id, {})
    
    def is_logged_in(self) -> bool:
        return self._current_user_id is not None
    
    def get_active_records(self, record_type: str = "recipes") -> List[dict]:
        if not self.is_logged_in():
            return []
        user_id = self._current_user_id
        prefix = f"{user_id}_"
        all_records = getattr(self, "_all_records", {})
        filtered = [r for r in all_records.get(record_type, []) if r["id"].startswith(prefix)]
        return filtered
    
    def add_record(self, record: dict) -> None:
        user = self.get_current_user()
        if not user or "id" not in record:
            raise ValueError("No active user or missing record ID")
        prefix = f"{user['id']}_"
        record["owner_id"] = user["id"]
        record["id"] = f"{prefix}{record.get('internal_id', '')}"
        
        if "_all_records" not in self.__dict__:
            self._all_records = {"recipes": [], "menus": [], "shopping_lists": []}
        
        target_list = self._all_records[record["type"]]
        target_list.append(record)
