# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: MealWorkshop
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str
    price_per_unit: float = 0.0

@dataclass
class Recipe:
    name: str
    ingredients: list[Ingredient] = field(default_factory=list)
    nutrition_notes: Optional[str] = None

@dataclass
class MenuDay:
    date: date
    breakfast: Optional[Recipe] = None
    lunch: Optional[Recipe] = None
    dinner: Optional[Recipe] = None

class MealWorkshopState:
    def __init__(self):
        self.recipes: dict[str, Recipe] = {}
        self.menus: list[MenuDay] = []
        
    def add_recipe(self, recipe: Recipe) -> None:
        self.recipes[recipe.name.lower()] = recipe
        
    def get_ingredients_for_day(self, day: MenuDay) -> list[Ingredient]:
        total_list = []
        for meal in [day.breakfast, day.lunch, day.dinner]:
            if meal:
                total_list.extend(meal.ingredients)
        return total_list

# Demo dataset initialization
demo_state = MealWorkshopState()

demo_recipe_1 = Recipe(
    name="Oatmeal Bowl",
    ingredients=[
        Ingredient("oats", 0.5, "cup"),
        Ingredient("milk", 1.0, "cup"),
        Ingredient("banana", 1.0, "piece")
    ],
    nutrition_notes="High in fiber and potassium."
)

demo_recipe_2 = Recipe(
    name="Grilled Chicken Salad",
    ingredients=[
        Ingredient("chicken breast", 0.3, "kg"),
        Ingredient("lettuce", 0.15, "head"),
        Ingredient("tomato", 2.0, "piece")
    ],
    nutrition_notes="Lean protein with vitamins A and C."
)

demo_state.add_recipe(demo_recipe_1)
demo_state.add_recipe(demo_recipe_2)

today = date.today()
demo_menu_day = MenuDay(
    date=today,
    breakfast=demo_recipe_1,
    lunch=demo_recipe_2,
    dinner=None
)
demo_state.menus.append(demo_menu_day)
