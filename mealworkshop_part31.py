# === Stage 31: Add compact table rendering for long lists ===
# Project: MealWorkshop
def render_compact_table(items, columns=None):
    if not items: return ""
    if columns is None: columns = list(next(iter(items.values())).keys())
    header = " | ".join(columns) + "\n" + "-" * (len(header) - 1) + "\n"
    rows = []
    for name, data in sorted(items.items(), key=lambda x: str(x[0]).lower()):
        row = " | ".join(str(data.get(col, ""))[:20] for col in columns)
        if len(row) > 60: row = "\n".join(f"  {line}" for line in row.split("\n"))
        rows.append(row)
    return header + "\n".join(rows)
