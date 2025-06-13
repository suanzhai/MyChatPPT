from dataclasses import dataclass

from model.slide_content import SlideContent


@dataclass
class Slide:
    layout: int
    content: SlideContent
