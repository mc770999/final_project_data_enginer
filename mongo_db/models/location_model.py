from dataclasses import dataclass, field
from typing import List

@dataclass
class Location:
    country_name: str  # שם המדינה
    region_txt: str  # שם האזור הגאוגרפי
    city: str  # שם העיר שבה התרחש האירוע
    latitude: float  # קו רוחב של מיקום האירוע
    longitude: float  # קו אורך של מיקום האירוע


    def __repr__(self):
        return (f"Location(country_name={self.country_name}, region_txt={self.region_txt}, "
                f"city={self.city}, latitude={self.latitude}, longitude={self.longitude})")
