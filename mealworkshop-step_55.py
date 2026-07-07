# === Stage 55: Add a setting to disable colorized output ===
# Project: MealWorkshop
class ColorMode:
    """Controls whether terminal output is colorized."""
    _enabled = True

    @classmethod
    def enable(cls):
        cls._enabled = True

    @classmethod
    def disable(cls):
        cls._enabled = False

    @classmethod
    def is_enabled(cls):
        return cls._enabled


def print_colored(text, color="red", enabled=None):
    """Print colored text if ColorMode allows it."""
    if enabled is not None:
        active = enabled
    else:
        active = ColorMode.is_enabled()
    if not active:
        print(text)
        return
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
    }
    reset = "\033[0m"
    print(f"{codes.get(color, '')}{text}{reset}")


def format_cost(total):
    """Format cost as currency string."""
    return f"${total:.2f}"


class Recipe:
    name = ""
    ingredients = []
    steps = []

    def __str__(self):
        lines = [f"Recipe: {self.name}", "Ingredients:", *self.ingredients, "---", "Steps:", *self.steps]
        return "\n".join(lines)


class ShoppingItem:
    name = ""
    quantity = 0.0
    price = 0.0

    def __str__(self):
        return f"{self.name}: {self.quantity:.1f} x ${self.price:.2f}"


class Menu:
    meals = []

    def add_meal(self, recipe):
        self.meals.append(recipe)

    def total_cost(self):
        return sum(r.ingredients[0].price for r in self.meals if hasattr(r, "ingredients") and r.ingredients)


def display_menu(menu, color=None):
    """Display menu items with optional color."""
    print_colored(f"Menu: {len(menu.meals)} meals", enabled=color is not None)
    for meal in menu.meals:
        print(meal)
