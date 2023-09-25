from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


def get_llm_chain(system_prompt_file):
    with open(system_prompt_file, "r") as file:
        system_prompt = file.read()
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),  # The persistent system prompt
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # Where the memory will be stored.
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),  # Where the human input will injected
        ]
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    conversation_with_memory = LLMChain(
        llm=ChatOpenAI(temperature=0), prompt=prompt, memory=memory
    )
    return conversation_with_memory


def generate_response(llm, text):
    response = llm.predict(human_input=text)
    return response
