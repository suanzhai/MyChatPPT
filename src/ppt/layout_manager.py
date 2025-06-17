from typing import Tuple

from model.slide_content import SlideContent
from ppt.layout_enum import LayoutEnum


class LayoutManager:
    def __init__(self):
        pass

    @staticmethod
    def get_layout(slide_content: SlideContent, layout_mapping: dict) -> Tuple[int, str]:
        if slide_content.bullet_points and len(slide_content.bullet_points) > 0 and slide_content.image_path:
            layout_enum = LayoutEnum.TITLE_CONTENT_PICTURE
        elif slide_content.bullet_points and len(slide_content.bullet_points) > 0 and not slide_content.image_path:
            layout_enum = LayoutEnum.TITLE_CONTENT
        elif (not slide_content.bullet_points or len(slide_content.bullet_points) == 0) and slide_content.image_path:
            layout_enum = LayoutEnum.TITLE_PICTURE
        else:
            layout_enum = LayoutEnum.TITLE_ONLY

        layout_id = layout_mapping.get(layout_enum.value, -1)

        return layout_id, str(layout_enum.value)