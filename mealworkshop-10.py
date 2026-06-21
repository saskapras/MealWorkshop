# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: MealWorkshop
class SearchEngine:
    def __init__(self, recipes):
        self.recipes = recipes
        self._index = {}
        for r in recipes:
            text = f"{r.get('name', '')} {r.get('category', '')} " \
                   + " ".join(r.get('ingredients', [])) + " " + str(r.get('cost', 0))
            words = set(text.lower().split())
            for word in words:
                if word not in self._index:
                    self._index[word] = []
                self._index[word].append(id(r))

    def search(self, query):
        normalized = query.strip().lower()
        if not normalized or len(normalized) < 2:
            return list(self.recipes.values())
        
        candidates = set()
        words = set(normalized.split())
        for word in words:
            if word in self._index:
                candidates.update(self._index[word])
        
        if not candidates:
            return []

        scored = []
        for rid in candidates:
            r = self.recipes[rid]
            score = 0.0
            
            name_match = r.get('name', '').lower()
            cat_match = r.get('category', '').lower()
            
            if word in name_match or word in cat_match:
                score += 1.5
            else:
                ingredients = [ing.lower() for ing in r.get('ingredients', [])]
                if word in ingredients:
                    score += 0.8
                
                cost_str = str(r.get('cost', 0))
                if word in cost_str:
                    score += 0.5
            
            nutrition = r.get('nutrition_notes', '')
            if word.lower() in nutrition.lower():
                score += 1.2

            scored.append((score, r))
        
        return [r for _, r in sorted(scored, key=lambda x: x[0], reverse=True)]
