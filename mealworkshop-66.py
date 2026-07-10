# === Stage 66: Add export of a short status dashboard ===
# Project: MealWorkshop
def status_dashboard(recipes, menus, shopping_lists):
    """Print a compact one-page dashboard of meal planning metrics."""
    print("=" * 50)
    print("MealWorkshop Status Dashboard")
    print("=" * 50)
    total_recipes = len(recipes) if recipes else 0
    total_menus = len(menus) if menus else 0
    total_lists = len(shopping_lists) if shopping_lists else 0
    print(f"Recipes loaded : {total_recipes}")
    print(f"Menus planned  : {total_menus}")
    print(f"Shopping lists : {total_lists}")
    print("=" * 50)

if __name__ == "__main__":
    status_dashboard([], [], [])
