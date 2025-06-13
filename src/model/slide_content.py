from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class SlideContent:
    title: str
    bullet_points: List[str] = field(default_factory=list)
    image_path: Optional[str] = None
