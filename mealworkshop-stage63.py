# === Stage 63: Add relationships between records where useful ===
# Project: MealWorkshop
from typing import Optional, Dict, List


def link_records(recipes: List[Recipe], menus: List[Menu],
                 shopping_lists: List[ShoppingList]) -> None:
    """Attach each menu to the recipes it uses and build a reverse map.

    For every recipe that appears in at least one menu we store the list of
    menus referencing it.  Likewise, for every ingredient used by any recipe
    we point back to the shopping lists that contain it — this makes it easy
    to fetch everything needed when planning a week's meals.
    """

    # --- recipes -> menus -------------------------------------------------
    menu_to_recipe: Dict[str, List[Menu]] = {}
    for menu in menus:
        for recipe_ref in menu.recipe_refs:
            key = recipe_ref.to_id() if hasattr(recipe_ref, 'to_id') else str(recipe_ref)
            menu_to_recipe.setdefault(key, []).append(menu)

    # --- ingredients -> shopping lists ------------------------------------
    ingredient_to_shopping: Dict[str, List[ShoppingList]] = {}
    for sl in shopping_lists:
        for item in sl.items:
            if hasattr(item, 'ingredient_id'):
                key = item.ingredient_id
            else:
                key = str(item)
            ingredient_to_shopping.setdefault(key, []).append(sl)

    # --- optional convenience helpers -------------------------------------
    recipes.recipe_menus = menu_to_recipe
    shopping_lists.shopping_for_ingredient = ingredient_to_shopping


def cross_reference_all() -> None:
    """Run the linking logic against whatever global containers exist.

    This is a no-op guard so that calling this function without any prior
    data does not raise — useful when the module is imported as part of a
    larger project and some records may still be missing.
    """
    try:
        link_records(getattr(globals(), 'recipes', []),
                     getattr(globals(), 'menus', []),
                     getattr(globals(), 'shopping_lists', []))
    except NameError:
        pass


def build_shopping_map() -> Dict[str, List[ShoppingList]]:
    """Return a mapping from ingredient id to the shopping lists that have it.

    This helper is exposed so other modules can query the cross-references
    without having to call ``link_records`` themselves — handy for reports
    and batch UI rendering.
    """
    link_records(getattr(globals(), 'recipes', []),
                 getattr(globals(), 'menus', []),
                 getattr(globals(), 'shopping_lists', []))
    return shopping_lists.shopping_for_ingredient if hasattr(shopping_lists, 'shopping_for_ingredient') else {}


def get_menus_for_recipe(recipe: Recipe) -> List[Menu]:
    """Return all menus that include the given recipe (or a reference to it)."""
    key = recipe.to_id() if hasattr(recipe, 'to_id') else str(recipe)
    return menu_to_recipe.get(key, [])
