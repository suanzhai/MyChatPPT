import re
from typing import Optional

from model.power_point import PowerPoint
from model.slide import Slide
from model.slide_content import SlideContent


class PowerPointParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(text: str, layout_mapping: dict) -> PowerPoint:
        lines = text.splitlines()

        presensation_title = ""
        slides = []
        current_slide: Optional[Slide] = None

        slide_title_pattern = re.compile(r'^##\s+(.*?)\s+\[(.*?)]')
        bullet_pattern = re.compile(r'^-\s+(.*)')
        image_pattern = re.compile(r'!\[.*?]\((.*?)\)')

        for line in lines:
            if line.startswith("# "):  # Presentation 文件名
                presensation_title = line[2:].strip()
            elif line.startswith("##"):  # slide 标题
                match = slide_title_pattern.match(line)
                if match:
                    title, layout = match.groups()
                    layout_index = layout_mapping.get(layout.strip(), 1)
                    if current_slide:
                        slides.append(current_slide)

                    current_slide = Slide(layout=layout_index, content=SlideContent(title=title, bullet_points=[]))
            elif line.startswith('- ') and current_slide:
                match = bullet_pattern.match(line)
                if match:
                    bullet = match.group(1).strip()
                    current_slide.content.bullet_points.append(bullet)
            elif line.startswith('![') and current_slide:
                match = image_pattern.match(line)
                if match:
                    image_path = match.group(1).strip()
                    current_slide.content.image_path = image_path

        if current_slide:
            slides.append(current_slide)

        return PowerPoint(presensation_title, slides)
