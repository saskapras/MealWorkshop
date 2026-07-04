# === Stage 51: Add unit tests for search and filter behavior ===
# Project: MealWorkshop
from unittest.mock import patch, MagicMock
import sys
sys.path.insert(0, '/path/to/mealworkshop')  # Adjust path as needed

def test_search_recipes_by_name():
    from mealworkshop.recipe_manager import RecipeManager
    manager = RecipeManager()
    recipes = [MagicMock(name='Pasta', calories=500), MagicMock(name='Salad', calories=300)]
    with patch.object(manager, '_recipes', new_callable=list) as mock_recipes:
        mock_recipes.extend(recipes)
        results = manager.search('Pasta')
        assert len(results) == 1 and results[0].name == 'Pasta'

def test_filter_by_calories():
    from mealworkshop.recipe_manager import RecipeManager
    manager = RecipeManager()
    recipes = [MagicMock(name='Light', calories=250), MagicMock(name='Heavy', calories=800)]
    with patch.object(manager, '_recipes', new_callable=list) as mock_recipes:
        mock_recipes.extend(recipes)
        results = manager.filter_by_calories(max_kcal=400)
        assert len(results) == 1 and results[0].name == 'Light'

def test_combined_search_and_filter():
    from mealworkshop.recipe_manager import RecipeManager
    manager = RecipeManager()
    recipes = [MagicMock(name='Chicken', calories=600), MagicMock(name='Fish', calories=350)]
    with patch.object(manager, '_recipes', new_callable=list) as mock_recipes:
        mock_recipes.extend(recipes)
        results = manager.search('Seafood') or []  # Fallback if search returns None
        filtered = [r for r in results if r.calories < 500]
        assert len(filtered) == 1 and filtered[0].name == 'Fish'
