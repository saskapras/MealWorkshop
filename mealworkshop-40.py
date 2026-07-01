# === Stage 40: Add plain text report export ===
# Project: MealWorkshop
def export_report(shop_list, menu_plan):
    with open("mealworkshop_report.txt", "w", encoding="utf-8") as f:
        f.write(f"=== MealWorkshop Report ===\n\n")
        if shop_list:
            total_cost = sum(item["cost"] for item in shop_list)
            f.write(f"Shopping List (Total Cost: {total_cost:.2f}):\n")
            for item in sorted(shop_list, key=lambda x: x.get("quantity", 0)):
                name = item.get("name", "Unknown")
                qty = item.get("quantity", 1)
                cost = item.get("cost", 0.0)
                f.write(f" - {qty}x {name}: {cost:.2f}\n")
            f.write("\n")
        if menu_plan:
            for day, meals in menu_plan.items():
                f.write(f"[{day}]\n")
                for meal_type, recipe_name in meals.items():
                    nutrition = recipe_name.get("nutrition_notes", "N/A")
                    f.write(f"  {meal_type.capitalize()}: {recipe_name['name']}\n")
                    if nutrition:
                        f.write(f"    Note: {nutrition}\n")
                f.write("\n")
        else:
            f.write("No menu plan found.\n")
