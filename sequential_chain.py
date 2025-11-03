from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Give detailed report on the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate 5 line summary on following text \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"wordl war 2"})

print(result)

chain.get_graph().print_ascii()


