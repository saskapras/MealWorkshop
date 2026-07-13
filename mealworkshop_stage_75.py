# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: MealWorkshop
def validate_recipe(recipe):
    warnings = []
    errors = []
    if recipe.get("name") is None:
        errors.append("Recipe missing 'name' field.")
    if recipe.get("ingredients") is None or len(recipe["ingredients"]) == 0:
        errors.append("Recipe has no ingredients listed.")
    else:
        for i, ing in enumerate(recipe["ingredients"]):
            if not isinstance(ing, dict) or "item" not in ing:
                warnings.append(f"Ingredient at index {i} is missing 'item' key.")
            if "amount" in ing and (not isinstance(ing["amount"], (int, float)) or ing["amount"] <= 0):
                errors.append(f"Ingredient '{ing['item']}' has invalid amount: {ing['amount']}.")
    if recipe.get("instructions") is None or len(recipe["instructions"]) == 0:
        warnings.append("Recipe instructions are empty; consider adding steps.")
    if "nutrition" in recipe and not isinstance(recipe["nutrition"], dict):
        warnings.append("'nutrition' field should be a dictionary with nutrient keys.")
    return errors, warnings
