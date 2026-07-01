# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: MealWorkshop
def repair_data_integrity(data):
    if 'recipes' in data:
        for r in data['recipes']:
            if r.get('ingredients'):
                missing = [i for i in r['ingredients'] if i.get('quantity') is None]
                for item in missing:
                    item['quantity'] = 1.0
    if 'menus' in data:
        for m in data['menus']:
            if not m.get('date'):
                from datetime import date, timedelta
                today = date.today()
                offset = (m.get('day_of_week', 1) - 1).days % 7 + 1
                m['date'] = (today + timedelta(days=offset)).isoformat()
    if 'shopping_lists' in data:
        for sl in data['shopping_lists']:
            if not sl.get('items'):
                sl['items'] = []
            for item in sl['items']:
                if item.get('recipe_id') and item.get('quantity') is None:
                    recipe = next((r for r in data.get('recipes', []) if r['id'] == item['recipe_id']), {})
                    default_qty = recipe.get('default_quantity', 1.0)
                    item['quantity'] = default_qty
    return data
