# === Stage 56: Add compact error classes for domain failures ===
# Project: MealWorkshop
class RecipeError(Exception):
    """Raised when a recipe definition is invalid."""
    pass


class MenuPlannedError(Exception):
    """Raised when a menu cannot be scheduled."""
    pass


class ShoppingListError(Exception):
    """Raised when inventory or cost data is inconsistent."""
    pass


class NutritionNoteError(Exception):
    """Raised when nutritional information is malformed."""
    pass
