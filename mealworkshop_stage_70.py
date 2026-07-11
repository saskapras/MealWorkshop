# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: MealWorkshop
import json, os

CONFIRMATION_FILE = "mealworkshop_confirmation.txt"

def clear_state():
    if not os.path.exists(CONFIRMATION_FILE):
        print("WARNING: clear_state() called without prior confirmation.")
        return False
    try:
        data = load_all_data()
        write_all_data(data)
        remove_all_files()
        os.remove(CONFIRMATION_FILE)
        print("MealWorkshop workspace completely cleared and reset to initial state.")
        return True
    except Exception as e:
        print(f"Error clearing state: {e}")
        return False

def confirm_clear():
    """Prompts user for confirmation to clear the entire MealWorkshop data."""
    choice = input("Are you sure you want to clear all data? Type 'yes' to confirm. ")
    if choice.lower() == "yes":
        with open(CONFIRMATION_FILE, "w") as f:
            f.write("confirmed\n")

if __name__ == "__main__":
    confirm_clear()
