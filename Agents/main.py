import streamlit as st
from skin_beauty_tips.makeup_artist import run_makeup_artist
from skin_beauty_tips.skincare_consultant import run_skincare_consultant
from skin_beauty_tips.beauty_trends_expert import run_beauty_trends_expert
from skin_beauty_tips.product_recommender import run_product_recommender

# Sidebar ke zariye agent selection
st.sidebar.title("💄 Beauty Assistant Agents")
agent_option = st.sidebar.radio("Select an Agent", (
    "Makeup Artist",
    "Skincare Consultant",
    "Beauty Trends Expert",
    "Product Recommender"
))

# Agent ke mutabiq function call
if agent_option == "Makeup Artist":
    run_makeup_artist()

elif agent_option == "Skincare Consultant":
    run_skincare_consultant()

elif agent_option == "Beauty Trends Expert":
    run_beauty_trends_expert()

elif agent_option == "Product Recommender":
    run_product_recommender()
