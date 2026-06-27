# === Stage 25: Add daily summary calculations ===
# Project: MealWorkshop
def calculate_daily_summary(menu):
    total_cost = sum(item['cost'] for item in menu if 'cost' in item)
    total_protein = sum(float(item.get('protein', 0)) for item in menu if 'nutrition' in item and isinstance(item['nutrition'], dict))
    total_carbs = sum(float(item.get('carbs', 0)) for item in menu if 'nutrition' in item and isinstance(item['nutrition'], dict))
    total_fats = sum(float(item.get('fat', 0)) for item in menu if 'nutrition' in item and isinstance(item['nutrition'], dict))
    return {
        "total_cost": round(total_cost, 2),
        "total_protein": round(total_protein, 1),
        "total_carbs": round(total_carbs, 1),
        "total_fats": round(total_fats, 1)
    }
