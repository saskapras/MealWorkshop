# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MealWorkshop
def delete_recipe(recipe_id: int, confirm_flag: bool = False) -> dict | None:
    if recipe_id in recipes_db:
        if confirm_flag or input(f"Удалить рецепт #{recipe_id}? (y/n): ").lower() == 'y':
            deleted_data = recipes_db.pop(recipe_id)
            return {"status": "deleted", "id": recipe_id, "data": deleted_data}
    return None
