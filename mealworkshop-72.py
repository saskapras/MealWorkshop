# === Stage 72: Add Markdown report export ===
# Project: MealWorkshop
def export_report(menus, recipes=None):
    """Export a compact Markdown report of all meal plans."""
    lines = ["# MealWorkshop Report\n"]
    for menu in menus:
        lines.append(f"## {menu.name}\n")
        if menu.date:
            lines.append(f"**Date:** {menu.date}\n")
        if menu.nutrition_note:
            lines.append(f"💡 *{menu.nutrition_note}*\n")
        for i, meal in enumerate(menu.meals):
            recipe = recipes.get(meal.recipe_id) if recipes else None
            ingredients = ", ".join(ing.name + f": {ing.quantity}" for ing in meal.ingredients)
            lines.append(f"{i+1}. **{meal.name}** — *{ingredients}*")
            if recipe and recipe.cost:
                lines.append(f"   💰 Cost: ${recipe.cost:.2f}")
        lines.append("\n---\n")
    return "\n".join(lines)
