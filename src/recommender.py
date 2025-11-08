#from langchain.chains import RetrievalQA
#from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever,api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", #stuff, map_reduce, refine, map_rerank
            retriever=retriever,
            chain_type_kwargs={"prompt": self.prompt},
            return_source_documents=True
        )
    def get_recommendations(self, query: str):
        result = self.qa_chain.run({"query": query})
        return result['result']    