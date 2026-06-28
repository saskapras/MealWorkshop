# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: MealWorkshop
from datetime import datetime, timedelta
import json
from typing import List, Dict, Any

def get_upcoming_items(data: Dict[str, Any], days_ahead: int = 7) -> List[Dict[str, Any]]:
    """Return upcoming meal reminders from the data structure."""
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    reminders = []

    if "scheduled_meals" not in data or not isinstance(data["scheduled_meals"], list):
        return reminders

    for item in data["scheduled_meals"]:
        try:
            meal_date_str = item.get("date")
            if not meal_date_str:
                continue
            meal_date = datetime.strptime(meal_date_str, "%Y-%m-%d").date()
            
            if now.date() <= meal_date <= cutoff.date():
                reminders.append({
                    "title": item.get("name", "Unknown Meal"),
                    "date": meal_date.isoformat(),
                    "recipe_id": item.get("recipe_id"),
                    "days_until": (meal_date - now.date()).days,
                    "status": item.get("status", "planned")
                })
        except ValueError:
            continue

    reminders.sort(key=lambda x: x["date"])
    return reminders
