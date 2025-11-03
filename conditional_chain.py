from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser ,PydanticOutputParser
from typing import Literal
from pydantic import BaseModel , Field
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
import os
from huggingface_hub import login

load_dotenv()

login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",  # best fine tune model
    task = "text-generation",
    temperature=0.7

)

model = ChatHuggingFace(llm=llm)

#pydantic output parser for controle on feedback sentiment either positive or negative

class feedback(BaseModel):

    sentiment : Literal["positive","negative"] = Field(description="Return sentiment of the review either negative, positive")

pydan_parser = PydanticOutputParser(pydantic_object=feedback)

#pydantic output parser to controle on reponse text by removing extra sentence except reponse

class response(BaseModel):
    response : str = Field(description="Wite a reponse lines for feedback ignore line which is not neccesry ") 

response_parser = PydanticOutputParser(pydantic_object=response)


#prompt for sentiment pass to - > pydan_parser
prompt1 = PromptTemplate(
    template="feedback -->{feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":pydan_parser.get_format_instructions()}
)

#chain which c;assify the sentiment into positive or negative

classify_chain = prompt1 | model | pydan_parser

#prompt2 and prompt3 for reponse pass to -> response parser

prompt2 = PromptTemplate(
    template="Write response to this positive feedback \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": response_parser.get_format_instructions()}
)

prompt3 = PromptTemplate(
    template="Write  appropriate response to this negative feedback \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": response_parser.get_format_instructions()}
)

#conditional chain decide which reponse is show at the end 

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=="positive", prompt2 | model | response_parser),
    (lambda x:x.sentiment=="negative" , prompt3 | model | response_parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

#final chain combine claasify and conditional chain 
chain = classify_chain | branch_chain

chain.get_graph().print_ascii()


