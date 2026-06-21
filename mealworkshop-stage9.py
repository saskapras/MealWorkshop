# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: MealWorkshop
class SortableMenu:
    def __init__(self, items):
        self.items = items
    
    def sort_by(self, key_func=None, reverse=False):
        if key_func is None:
            return sorted(self.items, key=lambda x: (x.get('title', ''), x.get('date', '')))
        return sorted(self.items, key=key_func, reverse=reverse)

def get_sort_key(item, field='priority'):
    val = item.get(field, 0)
    if isinstance(val, str):
        try:
            return int(val)
        except ValueError:
            return float('inf')
    return val or ''

# Usage example for sorting by priority (numeric), then title (alpha)
def sort_menu_items(items):
    items.sort(key=lambda x: (get_sort_key(x, 'priority'), x.get('title', ''), x.get('date', '')))
