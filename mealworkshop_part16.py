# === Stage 16: Add argparse support for the most common commands ===
# Project: MealWorkshop
import argparse

def main():
    parser = argparse.ArgumentParser(description="MealWorkshop CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    recipes_parser = subparsers.add_parser("recipes", help="Manage recipes")
    recipes_parser.add_argument("-l", "--list", action="store_true", help="List all recipes")
    recipes_parser.add_argument("-a", "--add", type=str, help="Add a new recipe (JSON)")
    
    menus_parser = subparsers.add_parser("menus", help="Manage weekly menus")
    menus_parser.add_argument("-c", "--create", type=str, help="Create menu from JSON")
    menus_parser.add_argument("-d", "--delete", type=int, help="Delete menu by ID")
    
    shopping_parser = subparsers.add_parser("shopping", help="Shopping list manager")
    shopping_parser.add_argument("-g", "--generate", action="store_true", help="Generate list from current menu")
    shopping_parser.add_argument("-r", "--remove", type=str, help="Remove item by name")
    
    costs_parser = subparsers.add_parser("costs", help="Calculate meal costs")
    costs_parser.add_argument("--menu-id", type=int, required=True, help="Menu ID to calculate for")
    
    nutrition_parser = subparsers.add_parser("nutrition", help="View nutrition notes")
    nutrition_parser.add_argument("-r", "--recipe", type=str, help="Recipe name or ID")

if __name__ == "__main__":
    args = parser.parse_args()
    if not hasattr(args, "command"):
        parser.print_help()
    else:
        print(f"Executing command: {args.command}")
