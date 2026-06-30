# === Stage 37: Add recommendations for the next useful action ===
# Project: MealWorkshop
from typing import Optional, List
import random
from datetime import date, timedelta

def generate_next_action_suggestions(current_date: date) -> List[str]:
    """Generate a list of actionable suggestions for the next meal planning step."""
    today = current_date.strftime("%Y-%m-%d")
    
    # Define possible action categories and their templates
    actions_pool = [
        "Review ingredients in your shopping list from {date} to see what needs restocking.",
        "Check if any recipes scheduled for {date} can be prepped today to save time later.",
        "Look at the nutrition notes for meals planned this week; consider swapping high-calorie items.",
        "Calculate total cost of ingredients used so far and compare against your weekly budget.",
        "Identify overlapping ingredients across multiple upcoming recipes to optimize shopping trips.",
        "Draft a simple menu for tomorrow based on available fresh produce in the fridge.",
        "Update the recipe difficulty tags if you found any steps too complex during recent cooking sessions.",
        "Set a reminder to clean and store leftovers from yesterday's dinner before 6 PM.",
        "Search online for one new vegetable substitute for an ingredient you dislike or lack.",
        "Print out the shopping list and cross off items as they are picked up at the store."
    ]
    
    # Select random actions based on current date context (simulating dynamic suggestions)
    selected_actions = []
    num_suggestions = 3
    
    for _ in range(num_suggestions):
        action_template = random.choice(actions_pool)
        formatted_action = action_template.format(date=today)
        
        # Ensure no duplicate actions are added to the list
        if formatted_action not in selected_actions:
            selected_actions.append(formatted_action)
    
    return selected_actions

# Example usage within a script context (uncomment when running standalone):
# next_steps = generate_next_action_suggestions(date.today())
# print("Recommended next actions:")
# for step in next_steps:
#     print(f"- {step}")
