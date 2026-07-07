# === Stage 57: Add structured result objects for command handlers ===
# Project: MealWorkshop
class MealResult:
    def __init__(self, status="success", message="", data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data.to_dict() if self.data else None,
        }

class MealErrorResult:
    def __init__(self, error_type="unknown", message="", original_error=None):
        self.error_type = error_type
        self.message = message
        self.original_error = str(original_error) if original_error else ""

    def to_dict(self):
        return {
            "status": "error",
            "message": self.message,
            "data": None,
            "error_type": self.error_type,
        }
