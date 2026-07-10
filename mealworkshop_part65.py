# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: MealWorkshop
def merge_ingredients(ingredient_lists):
    merged = {}
    for il in ingredient_lists:
        if isinstance(il, list):
            for item in il:
                key = str(item).lower()
                if key not in merged:
                    merged[key] = {"name": item, "quantity": 0, "unit": ""}
                else:
                    existing = merged[key]
                    if isinstance(item, tuple):
                        for i, val in enumerate(item):
                            existing[i] = val
                    elif isinstance(item, dict):
                        for k, v in item.items():
                            existing[k] = v
    return list(merged.values())
