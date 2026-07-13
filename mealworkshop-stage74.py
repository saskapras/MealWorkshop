# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: MealWorkshop
def compare_snapshots(old, new):
    """Compare two snapshot dicts and return a human-readable diff summary."""
    changes = []
    all_keys = set(list(old.keys()) + list(new.keys()))
    for key in sorted(all_keys):
        old_val = old.get(key)
        new_val = new.get(key)
        if old_val == new_val:
            continue
        if isinstance(old_val, str) and isinstance(new_val, str):
            changes.append(f"  {key}: \"{old_val}\" -> \"{new_val}\"")
        else:
            changes.append(f"  {key}: {old_val!r} -> {new_val!r}")
    return "\n".join(changes) if changes else "No changes detected."
