# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: MealWorkshop
import unittest
from mealworkshop.helpers import validate_recipe, calculate_shopping_cost

class TestHelpers(unittest.TestCase):
    def test_validate_valid_recipe(self):
        self.assertTrue(validate_recipe({"name": "Soup", "ingredients": [{"item": "Onion", "qty": 1}]}))
    
    def test_validate_missing_name(self):
        with self.assertRaises(ValueError):
            validate_recipe({"ingredients": []})
    
    def test_calculate_cost_empty_list(self):
        self.assertEqual(calculate_shopping_cost([]), 0.0)
    
    def test_calculate_cost_simple(self):
        items = [{"item": "Milk", "qty": 2, "price_per_unit": 1.5}]
        self.assertEqual(calculate_shopping_cost(items), 3.0)

if __name__ == "__main__":
    unittest.main()
