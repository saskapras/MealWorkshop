# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: MealWorkshop
def format_recipe_summary(recipe: dict) -> str:
    """Generate a concise human-readable summary for a recipe entry."""
    title = recipe.get("title", "Untitled")
    prep_time = recipe.get("prep_time_minutes", 0)
    servings = recipe.get("servings", 1)
    cost = recipe.get("cost_per_serving", 0.0)
    nutrition_highlights = recipe.get("nutrition_notes", [])

    lines = [f"Recipe: {title}"]
    if prep_time > 0:
        lines.append(f"Prep time: {prep_time} minutes")
    if servings != 1:
        lines.append(f"Serves: {servings}")
    cost_str = f"${cost:.2f}" if cost else "Cost: N/A"
    lines.append(cost_str)

    if nutrition_highlights:
        lines.append("Notes:")
        for note in nutrition_highlights[:3]:  # Limit to first 3 notes
            lines.append(f"- {note}")
    return "\n".join(lines)


def validate_shopping_list_item(item: dict, required_fields: list[str]) -> bool:
    """Check if a shopping list item contains all mandatory fields."""
    for field in required_fields:
        if not item.get(field):
            return False
    return True


def calculate_total_menu_cost(menu_items: list[dict], prices: dict[str, float]) -> float:
    """Compute the total estimated cost of a menu based on current ingredient prices."""
    total = 0.0
    for item in menu_items:
        name = item.get("ingredient", "")
        quantity = item.get("quantity", 1)
        if name in prices:
            unit_price = prices[name]
            total += quantity * unit_price
    return round(total, 2)


def filter_recipes_by_tag(recipes: list[dict], tag: str) -> list[dict]:
    """Return a new list containing only recipes that include the specified tag."""
    return [r for r in recipes if tag.lower() in (r.get("tags", []) or "").lower()]
