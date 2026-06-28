# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: MealWorkshop
from datetime import date, timedelta
import re

def parse_date_from_text(text: str) -> date | None:
    """Extracts a date from text using common formats and returns the parsed date."""
    patterns = [
        r'(\d{1,2})\.?(\d{1,2})\.?(\d{4})',  # DD.MM.YYYY or D.M.YYYY
        r'(\d{4})-(\d{1,2})-(\d{1,2})',      # YYYY-MM-DD
        r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2}),?\s+(\d{4})', # Month DD YYYY
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                groups = [int(g) for g in match.groups()]
                d1, m1, y1 = groups[0], groups[1], groups[2]
                
                # Adjust for 1-9 month format (DD.MM.YYYY style where M might be single digit)
                if len(str(groups[1])) == 1:
                    m1 = int(f"0{m1}")
                    
                return date(y1, m1, d1)
            except ValueError:
                continue
                
    raise ValueError("Unable to parse a valid date from the provided text.")

def generate_date_range(start_str: str, end_str: str) -> list[date]:
    """Generates a list of dates between two parsed strings."""
    start = parse_date_from_text(start_str)
    end = parse_date_from_text(end_str)
    
    if start > end:
        raise ValueError("Start date must be before or equal to the end date.")
        
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]
