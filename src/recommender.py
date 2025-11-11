# from langchain_community.chains import RetrievalQA
# #from langchain.chains.retrieval_qa.base import RetrievalQA
# #from langchain.chains import RetrievalQA


from src.prompt_template import get_anime_prompt

#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableMap
#from langchain_core.runnables import RunnableMap
from langchain_groq import ChatGroq

class AnimeRecommender:
    def __init__(self, retriever,api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()  
       
        self.qa_chain = (
            RunnableMap({
                "context": retriever,                # retriever takes input question → returns docs
                "question": RunnablePassthrough()    # passes question as-is
            })
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
    

    def get_recommendations(self, query: str):
        return self.qa_chain.invoke(query)


     