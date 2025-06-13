from pptx import Presentation


class TemplateLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_template(template_path: str) -> Presentation:
        ptrs = Presentation(template_path)
        return ptrs

    @staticmethod
    def get_layout_mapping(prs: Presentation) -> dict:
        layout_mapping = {}
        for idx, layout in enumerate(prs.slide_layouts):
            layout_mapping[layout.name] = idx
        return layout_mapping

    @staticmethod
    def print_layouts(prs: Presentation):
        for idx, layout in enumerate(prs.slide_layouts):
            print(layout.name)
