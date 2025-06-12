# beauty_trends_expert.py
from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

trends_agent = Agent(
    name="Beauty Trends Expert",
    instructions="You are a beauty trend expert. Share the latest makeup, skincare, and beauty trends from around the world.",
    model=model
)

async def generate_beauty_trends(user_input: str):
    return await Runner.run(trends_agent, user_input, run_config=config)

def run_beauty_trends_expert():
    st.title("📈 Beauty Trends Expert")
    user_input = st.text_input("Enter a category or trend topic (e.g., 'lipsticks 2025', 'K-beauty'):")

    if "trends_output" not in st.session_state:
        st.session_state.trends_output = ""

    if st.button("Get Trends"):
        if user_input:
            with st.spinner("Finding latest trends..."):
                try:
                    response = asyncio.run(generate_beauty_trends(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_beauty_trends(user_input))

                st.session_state.trends_output = response.final_output
        else:
            st.warning("Please enter a trend topic.")

    if st.session_state.trends_output:
        st.markdown("### 🔥 Trending Now")
        st.write(st.session_state.trends_output)


