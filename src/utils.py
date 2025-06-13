from pptx import Presentation


def remove_all_slides(prs: Presentation):
    # 获取底层 XML 元素列表并清空
    xml_slides = prs.slides._sldIdLst
    if xml_slides is not None:
        for i in range(len(prs.slides)):
            xml_slides.remove(xml_slides[0])
    print("所有默认幻灯片已被移除。")
