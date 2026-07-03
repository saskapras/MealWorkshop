# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: MealWorkshop
from datetime import date, timedelta
import random

def run_demo():
    today = date.today()
    menu_plan = [
        {"day": 1, "recipe_name": "Pasta Carbonara", "cost": 450},
        {"day": 2, "recipe_name": "Chicken Stir-Fry", "cost": 380},
        {"day": 3, "recipe_name": "Vegetable Soup", "cost": 150},
    ]
    
    print(f"=== MealWorkshop Demo Scenario ({today}) ===")
    for item in menu_plan:
        planned_date = today + timedelta(days=item["day"] - 1)
        print(f"\nDay {item['day']}: {planned_date.strftime('%d.%m')}, Dish: {item['recipe_name']} (Cost: {item['cost']} RUB)")
        
        # Simulate random nutrition note generation for demonstration
        notes = ["High Protein", "Low Carb", "Vegetarian Friendly"]
        if item["day"] == 1:
            print(f"  Note: {random.choice(notes)}")
            
    print("\nDemo completed successfully.")

if __name__ == "__main__":
    run_demo()
