from dataclasses import dataclass, field
from typing import List

from model.slide import Slide


@dataclass
class PowerPoint:
    title: str
    slides: List[Slide] = field(default_factory=list)
