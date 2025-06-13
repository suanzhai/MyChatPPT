import ppt.genarater
from parser import power_point_parser
from template import loader


def main():
    input_text = """
# ChatPPT_Demo

## ChatPPT Demo [Title]

## 2024 业绩概述 [Agenda]
- 总收入增长15%
- 市场份额扩大至30%

## 业绩图表 [Picture]
![业绩图表](images/performance_chart.png)

## 新产品发布 [Title Content Picture]
- 产品A: 特色功能介绍
- 产品B: 市场定位
![未来增长](images/forecast.png)
        """
    template_path = "../templates/Fair frames presentation.pptx"
    presentation = loader.TemplateLoader.load_template(template_path)
    lay_mapping = loader.TemplateLoader.get_layout_mapping(presentation)
    loader.TemplateLoader.print_layouts(presentation)

    power_point = power_point_parser.PowerPointParser.parse(input_text, lay_mapping)
    output_pptx_file_path = f"../outputs/{power_point.title}.pptx"
    ppt.genarater.PPTGenerator.generate(power_point, template_path, output_pptx_file_path)


if __name__ == "__main__":
    main()
