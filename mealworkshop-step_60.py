# === Stage 60: Add saved views for frequently used filters ===
# Project: MealWorkshop
class SavedView:
    """Persist frequently used filters as named views."""

    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def apply(self, menu):
        for key, value in self.filters.items():
            if hasattr(menu, key) and getattr(menu, key) is not None:
                setattr(menu, key, value)
