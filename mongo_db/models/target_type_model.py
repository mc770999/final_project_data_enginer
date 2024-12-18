from dataclasses import dataclass, field
from typing import List


@dataclass
class TargetType:
    target_type: str  # targtype1_txt
    target: str  # תיאור המטרה

    def __repr__(self):
        return f"TargetType({self.target_type}, {self.target})"