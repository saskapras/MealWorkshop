# === Stage 34: Add support for multiple local user profiles ===
# Project: MealWorkshop
import json, os
from pathlib import Path

class UserProfiles:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.profiles_file = self.data_dir / "profiles.json"
        if not self.data_dir.exists():
            self.data_dir.mkdir()
        self._load_profiles()

    def _load_profiles(self):
        try:
            with open(self.profiles_file, 'r', encoding='utf-8') as f:
                self.profiles = json.load(f)
        except FileNotFoundError:
            self.profiles = {}

    def add_profile(self, name, email=None, preferences=None):
        if not isinstance(preferences, dict):
            preferences = {}
        self.profiles[name] = {
            "email": email or "",
            "preferences": preferences,
            "created_at": os.popen('date +%s').read().strip()
        }
        self._save_profiles()

    def get_profile(self, name):
        return self.profiles.get(name)

    def _save_profiles(self):
        with open(self.profiles_file, 'w', encoding='utf-8') as f:
            json.dump(self.profiles, f, indent=2, ensure_ascii=False)
