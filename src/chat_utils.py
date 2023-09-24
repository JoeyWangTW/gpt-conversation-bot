from langchain.llms import OpenAI

def generate_response(text):

    llm = OpenAI()
    response = llm.predict(text)
    return response
