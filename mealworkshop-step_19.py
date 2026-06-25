# === Stage 19: Add undo support for the last simple mutation ===
# Project: MealWorkshop
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class UndoManager:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.max_history_size: int = 10

    def record(self, action_type: str, data: Dict[str, Any]) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "data": data
        }
        self.history.append(entry)
        if len(self.history) > self.max_history_size:
            self.history.pop(0)

    def undo_last(self) -> Optional[Dict[str, Any]]:
        if not self.history:
            return None
        
        last_entry = self.history[-1]
        action_type = last_entry["action"]
        data = last_entry["data"]
        
        # Revert based on action type
        if action_type == "add_recipe":
            recipe_id = data.get("id")
            for i, r in enumerate(self.recipes):
                if r.id == recipe_id:
                    self.recipes.pop(i)
                    break
        
        elif action_type == "update_recipe":
            recipe_id = data.get("id")
            old_data = data.get("old_values", {})
            # Assuming 'recipes' list exists in outer scope or passed as argument
            for r in self.recipes:
                if r.id == recipe_id:
                    r.name = old_data.get("name", r.name)
                    r.ingredients = old_data.get("ingredients", r.ingredients)
                    break
        
        elif action_type == "delete_recipe":
            recipe_id = data.get("id")
            for i, r in enumerate(self.recipes):
                if r.id == recipe_id:
                    self.recipes.pop(i)
                    break
                    
        # Remove from history after undoing (optional strategy)
        self.history.pop()
        
        return last_entry
