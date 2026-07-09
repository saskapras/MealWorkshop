# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: MealWorkshop
def score_recipe(recipe, preferences=None):
    """Score a recipe based on ingredient availability and dietary tags."""
    if preferences is None:
        preferences = {'vegetarian': False, 'vegan': False, 'gluten_free': False}
    score = 10.0
    for tag in preferences:
        if tag in recipe.get('tags', []) and recipe['tags'].count(tag) > 0:
            score += 2.0
        elif tag not in recipe.get('tags', []):
            score -= 3.0
    return round(score, 1)

def recommend_recipes(available_ingredients, recipes, preferences=None, top_n=5):
    """Recommend the best recipes from a list based on ingredient match and scoring."""
    if preferences is None:
        preferences = {'vegetarian': False, 'vegan': False}
    scored = []
    for recipe in recipes:
        matched = sum(1 for ing in available_ingredients if ing.lower() in [i.lower() for i in recipe.get('ingredients', [])])
        score = score_recipe(recipe, preferences) + (matched / max(len(available_ingredients), 1)) * 30.0
        scored.append((score, recipe['name'], matched))
    ranked = sorted(scored, key=lambda x: (-x[0], -x[2]))
    return ranked[:top_n]
