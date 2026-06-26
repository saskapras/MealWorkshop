# === Stage 24: Add grouped summaries by category or status ===
# Project: MealWorkshop
def generate_grouped_summary(recipes, categories=None):
    if not recipes: return {}
    groups = {cat: [] for cat in set(r.get('category', 'Uncategorized') for r in recipes)} if categories is None else {cat: [] for cat in categories}
    uncategorized = [r for r in recipes if (groups := {}).get(r.get('category', 'Other'), [])]
    for recipe in recipes:
        key = recipe.get('category', 'Uncategorized') or 'Other'
        groups.setdefault(key, []).append(recipe)
    summary = {k: {'count': len(v), 'items': v[:3]} for k, v in sorted(groups.items(), key=lambda x: x[0])}
    return summary
