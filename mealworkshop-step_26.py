# === Stage 26: Add weekly summary calculations ===
# Project: MealWorkshop
def calculate_weekly_summary(recipes, days=7):
    total_cost = sum(r.get('total_cost', 0) for r in recipes if 'cost' in r)
    avg_protein = sum(r.get('nutrition', {}).get('protein', 0) for r in recipes) / max(len(recipes), 1)
    unique_ingredients = set()
    for recipe in recipes:
        unique_ingredients.update(recipe.get('ingredients', []))
    return {
        'total_cost': round(total_cost, 2),
        'avg_protein_per_meal': round(avg_protein, 2),
        'unique_ingredient_count': len(unique_ingredients)
    }
