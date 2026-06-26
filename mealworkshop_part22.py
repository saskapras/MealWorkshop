# === Stage 22: Add favorite records and quick favorite listing ===
# Project: MealWorkshop
class FavoriteManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.favorites_file = os.path.join(repo_path, "data", "favorites.json")
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
        if not os.path.exists(os.path.join(self.repo_path, "data")):
            os.makedirs(os.path.join(self.repo_path, "data"))

    def add_favorite(self, recipe_id, notes=""):
        favorites = self._load_favorites()
        if recipe_id in favorites:
            return False
        favorites[recipe_id] = {"notes": notes}
        self._save_favorites(favorites)
        return True

    def remove_favorite(self, recipe_id):
        favorites = self._load_favorites()
        if recipe_id not in favorites:
            return False
        del favorites[recipe_id]
        self._save_favorites(favorites)
        return True

    def get_favorites(self):
        return self._load_favorites()

    def _load_favorites(self):
        try:
            with open(self.favorites_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_favorites(self, data):
        os.makedirs(os.path.dirname(self.favorites_file), exist_ok=True)
        with open(self.favorites_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
