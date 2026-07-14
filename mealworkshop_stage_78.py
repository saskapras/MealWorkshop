# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: MealWorkshop
def _format_ingredient_row(ingredient, qty, unit):
    """Return a single shopping-list row as (name, quantity, unit)."""
    return ingredient.strip(), float(qty), unit.strip()


def build_shopping_list(items):
    """Convert a list of raw strings into structured rows."""
    rows = []
    for item in items:
        parts = item.split("|")
        name, qty_str, unit = parts[0].strip(), parts[1].strip(), parts[2].strip()
        try:
            qty = float(qty_str)
        except ValueError:
            qty = 0.0
        rows.append((name, qty, unit))
    return rows


def calculate_total_cost(rows, prices):
    """Sum cost for each row using the price dictionary."""
    total = 0.0
    for name, qty, _ in rows:
        if name in prices and qty > 0:
            total += prices[name] * qty
    return round(total, 2)


def format_cost_summary(total):
    """Return a short readable cost summary string."""
    if total <= 0.5:
        label = "very cheap"
    elif total <= 3.0:
        label = "affordable"
    elif total <= 8.0:
        label = "moderate"
    else:
        label = "expensive"
    return f"${total:.2f} ({label})"
