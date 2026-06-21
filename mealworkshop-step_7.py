# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: MealWorkshop
def format_recipe(recipe):
    print(f"Title: {recipe['title']}")
    print(f"Cooking time: {recipe.get('cooking_time', 'N/A')} min")
    if recipe.get('ingredients'):
        print("Ingredients:")
        for ing in sorted(recipe['ingredients'], key=lambda x: x[0]):
            print(f"  - {ing}")
    if recipe.get('nutrition'):
        print(f"Nutrition: {recipe['nutrition']} kcal per serving")

def format_menu(menu):
    print("Menu:")
    for day, items in menu.items():
        print(f"{day}:")
        for item in items:
            cost = f" ({item.get('cost', 0)} RUB)" if isinstance(item.get('cost'), (int, float)) else ""
            print(f"  - {item['name']}{cost}")

def format_shopping_list(items):
    total_cost = sum(float(i.get('cost', 0)) for i in items)
    print("Shopping List:")
    for item in sorted(items, key=lambda x: x[0]):
        count = item.get('count', 1)
        unit = item.get('unit', 'pcs')
        cost = f" ({item.get('cost', 0)} RUB)" if isinstance(item.get('cost'), (int, float)) else ""
        print(f"  - {count}x {item['name']} {unit}{cost}")
    print(f"Total estimated cost: {total_cost:.2f} RUB")
