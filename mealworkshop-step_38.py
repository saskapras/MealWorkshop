# === Stage 38: Add data integrity checks for broken references ===
# Project: MealWorkshop
def validate_references(recipes, menus):
    broken = []
    for r in recipes:
        if r.get('author_id') and r['author_id'] not in [m['id'] for m in menus]:
            broken.append(f"Recipe {r['name']} references unknown author_id={r['author_id']}")
        for ing in r.get('ingredients', []):
            if ing.get('source_recipe'):
                src = next((x for x in recipes if x['id'] == ing['source_recipe']), None)
                if not src:
                    broken.append(f"Recipe {r['name']} references missing source_recipe={ing['source_recipe']}")
    return broken
