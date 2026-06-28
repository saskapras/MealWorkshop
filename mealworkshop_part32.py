# === Stage 32: Add pagination helpers for long console output ===
# Project: MealWorkshop
def format_table(data: list, columns: list) -> str:
    if not data: return "No data."
    widths = [max(len(str(item)) for item in col) for col in zip(*[list(d.values()) for d in data] + [[c] * len(data)])]
    header = " | ".join(c.ljust(widths[i]) for i, c in enumerate(columns))
    row_fmt = " | ".join("{:<{w}}" for w in widths)
    lines = [header]
    if data:
        lines.append("-+-".join("-" * w for w in widths))
        lines.extend(row_fmt.format(*d.values(), **{"<": "<", ">": ">"}) for d in data)
    return "\n".join(lines)

def paginate_output(text: str, max_lines: int = 10):
    lines = text.splitlines()
    if len(lines) <= max_lines: return text
    chunks = []
    start = 0
    while start < len(lines):
        end = min(start + max_lines, len(lines))
        chunk = "\n".join(lines[start:end])
        if end == len(lines): break
        chunk += f"\n\n... ({len(lines) - end} more lines) ..."
        chunks.append(chunk)
        start = end
    return "\n\n---\n\n".join(chunks)
