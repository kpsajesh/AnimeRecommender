import streamlit as st
from pipeline.recommendation_pipeline import AnimeRecommendationPipeline

from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource 
def get_recommendation_pipeline():
    return AnimeRecommendationPipeline()

# pipeline = init_recommendation_pipeline()
pipeline = get_recommendation_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences. eg: Light hearted anime with school setting")
if query:
    with st.spinner("Generating recommendations for you..."):
        recommendations = pipeline.recommend(query)
    st.markdown("Recommended Anime:")
    st.write(recommendations)