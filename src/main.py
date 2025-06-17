
import ppt.genarater
import gradio as gr

from llm.ppt_agent import PPTAgent
from logger import LOG
from parser import power_point_parser
from template import loader

ppt_agent = PPTAgent()

def handle_conversation(content):
    bot_message = ppt_agent.chat_with_history(content)  # 获取聊天机器人的回复
    template_path = "templates/MasterTemplate.pptx"
    presentation = loader.TemplateLoader.load_template(template_path)
    lay_mapping = loader.TemplateLoader.get_layout_mapping(presentation)
    loader.TemplateLoader.print_layouts(presentation)

    power_point = power_point_parser.PowerPointParser.parse(bot_message, lay_mapping)
    file_name = f"{power_point.title}.pptx"
    output_pptx_file_path = f"outputs/{power_point.title}.pptx"
    ppt.genarater.PPTGenerator.generate(power_point, template_path, output_pptx_file_path)

    LOG.info(f"[ChatBot]: {bot_message}")  # 记录聊天机器人的回复
    return output_pptx_file_path

def main():
    with gr.Blocks(title="PPT生成") as language_mentor_app:
        with gr.Tab("PPT生成"):
            gr.Markdown("## PPT生成 ")  # 对话练习说明
            user_input = gr.Textbox(placeholder="PPT内容")
            button = gr.Button()
            button.click(handle_conversation, inputs=[user_input], outputs=gr.File())

    # 启动应用
    language_mentor_app.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    main()
