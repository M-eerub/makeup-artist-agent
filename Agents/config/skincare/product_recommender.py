# product_recommender.py
from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

product_agent = Agent(
    name="Product Recommender",
    instructions="You are a beauty product specialist. Recommend makeup and skincare products based on preferences, budget, and skin profile.",
    model=model
)

async def generate_product_recommendations(user_input: str):
    return await Runner.run(product_agent, user_input, run_config=config)

def run_product_recommender():
    st.title("🛍️ Beauty Product Recommender")
    user_input = st.text_area("What kind of product are you looking for? (e.g., budget mascara, SPF for oily skin)")

    if "product_output" not in st.session_state:
        st.session_state.product_output = ""

    if st.button("Recommend Products"):
        if user_input:
            with st.spinner("Searching for the best products for you..."):
                try:
                    response = asyncio.run(generate_product_recommendations(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_product_recommendations(user_input))

                st.session_state.product_output = response.final_output
        else:
            st.warning("Please enter what you're looking for.")

    if st.session_state.product_output:
        st.markdown("### 🧴 Recommended Products")
        st.write(st.session_state.product_output)
