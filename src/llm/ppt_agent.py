import random
import uuid

from langchain_core.messages import AIMessage

from llm.agent_base import AgentBase
from llm.session_history import get_session_history
from logger import LOG


class PPTAgent(AgentBase):
    def __init__(self):
        prompt_file =  "prompts/formatter.txt"
        super().__init__(
            name='PPT生成',
            prompt_file=prompt_file
        )

    def start_new_session(self, session_id: str = None):
        if not session_id:
            session_id = self.name + str(uuid.uuid4())

        history = get_session_history(session_id)
        LOG.info(f"[history][{session_id}]:{history}")

        if not history.messages:
            first_message = AIMessage(content=random.choice(self.intro))
            history.add_message(first_message)

        return history.messages[-1].content