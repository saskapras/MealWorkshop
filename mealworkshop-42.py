# === Stage 42: Add CSV export without external dependencies ===
# Project: MealWorkshop
def export_data_to_csv(data, filename):
    import csv
    if isinstance(data, dict) and data:
        fieldnames = list(data[0].keys())
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    elif isinstance(data, (list, tuple)) and data[0] if len(data) > 0 else False:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            for item in data:
                csv_line = ','.join(str(v) for v in item.values() if isinstance(item, dict)) or ','.join(map(str, item))
                f.write(csv_line + '\n')
