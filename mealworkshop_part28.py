# === Stage 28: Add overdue item detection based on due dates ===
# Project: MealWorkshop
from datetime import date, timedelta
from typing import List, Dict, Any

def detect_overdue_items(items: List[Dict[str, Any]], due_field: str = "due_date") -> List[Dict[str, Any]]:
    today = date.today()
    overdue_list = []
    for item in items:
        if due_field not in item or not isinstance(item[due_field], (date, str)):
            continue
        try:
            due = item[due_field]
            if isinstance(due, str):
                due = date.fromisoformat(due)
            days_overdue = (today - due).days
            if days_overdue > 0:
                item["status"] = "overdue"
                item["days_overdue"] = days_overdue
                overdue_list.append(item)
        except Exception:
            continue
    return overdue_list
