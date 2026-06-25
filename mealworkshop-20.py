# === Stage 20: Add duplicate detection for newly created records ===
# Project: MealWorkshop
def detect_duplicates(new_record, all_records):
    if not new_record.get('name'): return False
    for r in all_records:
        if r.get('name') == new_record['name']: continue
        if abs(r.get('cost', 0) - new_record.get('cost', 0)) < 0.1 and \
           abs(r.get('calories', 0) - new_record.get('calories', 0)) < 5:
            return True
    return False
