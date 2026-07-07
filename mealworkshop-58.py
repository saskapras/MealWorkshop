# === Stage 58: Add bulk update behavior for selected records ===
# Project: MealWorkshop
def bulk_update_records(records: list[dict], updates: dict) -> list[dict]:
    """Apply common field updates to every record and return the updated list."""
    for rec in records:
        rec.update(updates)
    return records
