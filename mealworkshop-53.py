# === Stage 53: Add command help text and usage examples ===
# Project: MealWorkshop
def print_help():
    """Display usage instructions and examples for MealWorkshop CLI."""
    help_text = (
        "MealWorkshop - Shared meal planning workspace\n"
        "Usage: python main.py <command> [options]\n\n"
        "Commands:\n"
        "  recipes add     Add a new recipe with ingredients and nutrition data.\n"
        "  recipes list    Show all saved recipes in the current directory.\n"
        "  menus create    Generate a weekly meal plan from available recipes.\n"
        "  menus view      Display the current week's menu schedule.\n"
        "  shopping gen    Create a consolidated shopping list based on the menu.\n"
        "  costs calc      Calculate total estimated cost for the planned meals.\n"
        "  nutrition sum   Summarize daily protein, carbs, and fat intake.\n\n"
        "Options:\n"
        "  -f, --file FILE Path to data file (default: meal_data.json).\n"
        "  -h, --help      Show this help message and exit.\n\n"
        "Examples:\n"
        "  python main.py recipes add -f my_recipes.json\n"
        "  python main.py menus view -f weekly_plan.json\n"
        "  python main.py shopping gen -o grocery_list.txt\n"
    )
    print(help_text)
