# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: MealWorkshop
def manage_tags(tags: dict, item_id: str) -> tuple[dict, list[str]]:
    """Add or remove tags for an item and generate a tag summary."""
    if "tags" not in item_id:
        return tags, []
    
    action = item_id.get("action", "")
    new_tags = item_id.get("new_tags", [])
    removed_tags = item_id.get("removed_tags", [])
    
    current_tags = tags.get(item_id["id"], set())
    
    if action == "add":
        for t in new_tags:
            current_tags.add(t)
    elif action == "remove":
        for t in removed_tags:
            current_tags.discard(t)
    
    updated_item = {**item_id, "tags": list(current_tags)}
    tags[item_id["id"]] = current_tags
    
    summary_lines = [f"Item '{updated_item['name']}' now has {len(current_tags)} tag(s)."]
    if new_tags:
        summary_lines.append(f"Added: {', '.join(new_tags)}.")
    if removed_tags:
        summary_lines.append(f"Removed: {', '.join(removed_tags)}.")
    
    return tags, summary_lines
