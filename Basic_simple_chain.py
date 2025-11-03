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

prompt = PromptTemplate(
    template="Write 5 key points in simple words about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result  =  chain.invoke({"topic":"ChatGPT 4"})

print(result)

chain.get_graph().print_ascii()