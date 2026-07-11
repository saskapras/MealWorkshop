# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: MealWorkshop
import re, datetime

def changelog_from_log(log_path):
    entries = []
    with open(log_path) as f:
        for raw in f.readlines():
            line = raw.strip()
            if not line or line.startswith('#'): continue
            m = re.match(r'(\d+):\s*(.*)', line)
            if m:
                idx, note = m.group(1), m.group(2).strip().rstrip('.')
                entries.append(f'- Step {idx}: {note}')
    today = datetime.date.today().strftime('%Y-%m-%d')
    return f'# MealWorkshop Changelog\nGenerated: {today}\n## Steps\n' + '\n'.join(entries)
