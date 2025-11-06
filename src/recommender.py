#from langchain.chains import RetrievalQA
#from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

#class AnimeRecommender:
#    def __init__(self, 