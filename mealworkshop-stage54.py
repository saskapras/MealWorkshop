# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: MealWorkshop
def colorize(text, code):
    return f"\033[{code}m{text}\033[0m"

class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def print_header(text):
    return f"{Color.BOLD}{Color.CYAN}{text}{Color.END}"

def print_success(text):
    return f"{Color.GREEN}{text}{Color.END}"

def print_error(text):
    return f"{Color.RED}{text}{Color.END}"

def print_warning(text):
    return f"{Color.YELLOW}{text}{Color.END}"

def format_recipe(recipe):
    lines = []
    for key, value in recipe.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)

def print_menu(menu):
    output = []
    output.append(print_header("Weekly Meal Plan"))
    for day, items in menu.items():
        output.append(f"--- {day} ---")
        for item in items:
            price_str = f"${item['price']:.2f}" if 'price' in item else ""
            nutrition_note = f" ({item.get('nutrition', '')})" if 'nutrition' in item else ""
            output.append(f"  {item['name']} [{price_str}]{nutrition_note}")
    return "\n".join(output)

def print_shopping_list(items):
    total = sum(item['cost'] for item in items if isinstance(item, dict))
    lines = []
    for name, qty, cost in items:
        lines.append(f"  {qty}x {name}: ${cost:.2f}")
    lines.append(f"\nTotal: ${total:.2f}")
    return "\n".join(lines)

def format_cost_report(costs):
    total = sum(costs.values()) if isinstance(costs, dict) else 0
    parts = []
    for item, amount in costs.items():
        parts.append(f"{item}: ${amount:.2f}")
    return f"{' | '.join(parts)} => Total: ${total:.2f}"

def print_nutrition_summary(items):
    macros = {"Protein": 0, "Carbs": 0, "Fat": 0}
    for item in items:
        if isinstance(item, dict) and 'macros' in item:
            macros.update(item['macros'])
    return f"Total Macros - Protein: {macros['Protein']}g | Carbs: {macros['Carbs']}g | Fat: {macros['Fat']}g"

def print_full_report(recipe=None, menu=None, shopping_list=None, costs=None, nutrition_summary=None):
    parts = []
    if recipe:
        parts.append(f"\n{print_header('Recipe')}")
        parts.append(format_recipe(recipe))
    if menu:
        parts.append(f"\n{print_header('Menu')}")
        parts.append(print_menu(menu))
    if shopping_list:
        parts.append(f"\n{print_header('Shopping List')}")
        parts.append(print_shopping_list(shopping_list))
    if costs:
        parts.append(f"\n{print_header('Cost Report')}")
        parts.append(format_cost_report(costs))
    if nutrition_summary:
        parts.append(f"\n{print_header('Nutrition Summary')}")
        parts.append(print_nutrition_summary(nutrition_summary))
    return "\n".join(parts)
