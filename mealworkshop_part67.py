# === Stage 67: Add a function that returns key project metrics ===
# Project: MealWorkshop
def project_metrics():
    total_recipes = len(Recipes)
    total_menues = len(Menus)
    total_shopping_lists = len(ShoppingLists)
    total_notes = sum(len(notes.values()) for n in NutritionNotes.values() if isinstance(n, dict))
    return {
        "total_recipes": total_recipes,
        "total_menues": total_menues,
        "total_shopping_lists": total_shopping_lists,
        "total_nutrition_notes": total_notes,
    }
