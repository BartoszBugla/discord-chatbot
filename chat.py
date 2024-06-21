from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage

from env import MODEL_PATH


class Chat:
    def __init__(self):
        self.llm = LlamaCpp(
            model_path=MODEL_PATH,
            n_ctx=128,
            n_threads=6,
            n_gpu_layers=99,
            n_batch=64,
            f16_kv=True,
            verbose=False,
            streaming=True,
        )

        self.chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=(
                        "You are a helpful assistant named Bob, that is always ready to help. "
                        "Just answer the user input."
                    )
                ),
                HumanMessagePromptTemplate.from_template("{text}."),
            ]
        )

        print("Chatbot initialized")

    def invoke(self, question):
        messages = self.chat_template.format_messages(text=question)

        return self.llm.invoke(
            input=messages,
            max_tokens=64,
            temperature=0.2,
            top_p=0.1,
        )
