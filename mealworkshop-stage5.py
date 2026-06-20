# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: MealWorkshop
def update_recipe(recipe_id, updates):
    if recipe_id in recipes:
        for key, value in updates.items():
            if key in recipes[recipe_id]:
                recipes[recipe_id][key] = value
            else:
                raise KeyError(f"Field '{key}' does not exist in recipe {recipe_id}")
        return True
    else:
        print(f"Recipe with ID {recipe_id} not found. No update performed.")
        return False

def update_menu_item(menu_id, item_index, updates):
    if menu_id in menus and 0 <= item_index < len(menus[menu_id]):
        for key, value in updates.items():
            if key in menus[menu_id][item_index]:
                menus[menu_id][item_index][key] = value
            else:
                raise KeyError(f"Field '{key}' does not exist in menu item {menu_id}:{item_index}")
        return True
    else:
        print(f"Menu ID {menu_id} or index {item_index} is invalid. No update performed.")
        return False

def add_shopping_item(shopping_list, category, name, quantity=1):
    if shopping_list not in shopping_lists:
        print(f"Shopping list '{shopping_list}' does not exist. Cannot add item.")
        return False
    key = f"{category}:{name}"
    if key in shopping_lists[shopping_list]:
        existing = shopping_lists[shopping_list][key]
        existing['quantity'] += quantity
        existing['last_updated'] = datetime.now().isoformat()
    else:
        shopping_lists[shopping_list][key] = {'name': name, 'category': category, 'quantity': quantity}
    return True

def update_shopping_item(shopping_list, key, updates):
    if shopping_list not in shopping_lists or key not in shopping_lists[shopping_list]:
        print(f"Item '{key}' not found in shopping list '{shopping_list}'.")
        return False
    for field_name, value in updates.items():
        if field_name in shopping_lists[shopping_list][key]:
            shopping_lists[shopping_list][key][field_name] = value
        else:
            raise KeyError(f"Field '{field_name}' does not exist.")
    return True
