import re
from typing import Optional

from model.power_point import PowerPoint
from model.slide import Slide
from model.slide_content import SlideContent
from ppt.layout_manager import LayoutManager


class PowerPointParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(text: str, layout_mapping: dict) -> PowerPoint:
        lines = text.splitlines()

        presensation_title = ""
        slides = []
        current_slide: Optional[Slide] = None

        bullet_pattern = re.compile(r'^-\s+(.*)')
        image_pattern = re.compile(r'!\[.*?]\((.*?)\)')

        for line in lines:
            if line.startswith("# "):  # Presentation 文件名
                presensation_title = line[2:].strip()
            elif line.startswith("##"):  # slide 标题
                title = line[3:].strip()
                if current_slide:
                    slides.append(current_slide)

                current_slide = Slide(layout=-1, content=SlideContent(title=title, bullet_points=[]))
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

        for slide in slides:
            slide.layout = LayoutManager.get_layout(slide.content, layout_mapping)[0]

        return PowerPoint(presensation_title, slides)
