# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: MealWorkshop
SETTINGS = {
    "currency": "RUB",
    "default_servings": 4,
    "unit_costs": {"kg": 150.0, "l": 80.0},
    "nutrition_notes_enabled": True,
}


def update_settings(key: str, value) -> None:
    if key in SETTINGS and not isinstance(SETTINGS[key], bool):
        SETTINGS[key] = value
