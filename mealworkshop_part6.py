# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MealWorkshop
def delete_recipe(recipe_id: int, confirm_flag: bool = False) -> dict | None:
    if recipe_id in recipes_db:
        if confirm_flag or input(f"Удалить рецепт #{recipe_id}? (y/n): ").lower() == 'y':
            deleted_data = recipes_db.pop(recipe_id)
            return {"status": "deleted", "id": recipe_id, "data": deleted_data}
    return None

# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MealWorkshop
def delete_item(item_id, confirm=False):
    if item_id in recipes:
        if confirm or input(f"Удалить рецепт #{item_id}? (y/n) ") == "y":
            del recipes[item_id]
            print(f"Рецепт #{item_id} удален.")
            return True
    elif item_id in menus:
        if confirm or input(f"Удалить меню #{item_id}? (y/n) ") == "y":
            del menus[item_id]
            print(f"Меню #{item_id} удалено.")
            return True
    elif item_id in shopping_lists:
        if confirm or input(f"Удалить позицию из списка покупок #{item_id}? (y/n) ") == "y":
            del shopping_lists[item_id]
            print(f"Позиция из списка покупок удалена.")
            return True
    elif item_id in nutrition_notes:
        if confirm or input(f"Удалить заметку о питании #{item_id}? (y/n) ") == "y":
            del nutrition_notes[item_id]
            print(f"Заметка о питании удалена.")
            return True
    else:
        print("ID не найден в базе данных.")
        return False
