# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: MealWorkshop
import unittest
from mealworkshop.app import MealWorkshop, Recipe

class TestMealWorkshopEdgeCases(unittest.TestCase):
    def setUp(self):
        self.ws = MealWorkshop()
        
    def test_delete_nonexistent_recipe(self):
        with self.assertRaises(ValueError) as context:
            recipe_id = "999"
            self.ws.delete_recipe(recipe_id)
        self.assertIn("not found", str(context.exception))

    def test_update_missing_fields(self):
        recipe = Recipe(name="Test", ingredients=["A"], steps=["1"])
        self.ws.add_recipe(recipe)
        with self.assertRaises(ValueError) as context:
            updated = Recipe(name="", ingredients=[], steps=[])
            self.ws.update_recipe(recipe.id, updated)
        self.assertIn("cannot be empty", str(context.exception))

    def test_update_nonexistent_recipe(self):
        with self.assertRaises(ValueError) as context:
            recipe_id = "999"
            new_recipe = Recipe(name="New", ingredients=["B"], steps=["2"])
            self.ws.update_recipe(recipe_id, new_recipe)
        self.assertIn("not found", str(context.exception))

    def test_update_with_empty_steps(self):
        recipe = Recipe(name="Test", ingredients=["A"], steps=["1"])
        self.ws.add_recipe(recipe)
        with self.assertRaises(ValueError) as context:
            updated = Recipe(name="Updated", ingredients=["B"], steps=[])
            self.ws.update_recipe(recipe.id, updated)
        self.assertIn("steps cannot be empty", str(context.exception))

if __name__ == "__main__":
    unittest.main()
