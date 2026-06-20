# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: MealWorkshop
def validate_recipe_id(recipe_id):
    if not recipe_id:
        raise ValueError("Recipe ID cannot be empty")
    if len(recipe_id) > 10:
        raise ValueError("Recipe ID must be less than or equal to 10 characters")
    return True

def validate_ingredient_name(name):
    if not name.strip():
        raise ValueError("Ingredient name cannot be empty")
    if len(name) < 2:
        raise ValueError("Ingredient name is too short")
    return True

def validate_short_text(text, max_length=50):
    if text and (len(text) > max_length or not text.strip()):
        raise ValueError(f"Text must be between 1 and {max_length} characters")
    return True
