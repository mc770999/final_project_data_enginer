from dataclasses import dataclass, field
from typing import List

@dataclass
class Date:
    day: str  # שם המדינה
    month: str  # שם האזור הגאוגרפי
    year: str  # שם העיר שבה התרחש האירוע


    def __repr__(self):
        return (f"Date(day={self.day}, month={self.month}, "
                f"year={self.year})")
