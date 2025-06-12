from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

makeup_agent = Agent(
    name="Makeup Artist",
    instructions="You are a professional makeup artist. Provide makeup tips, tutorials, and advice based on the user's skin type, tone, or occasion.",
    model=model
)

async def generate_makeup_advice(user_input: str):
    return await Runner.run(makeup_agent, user_input, run_config=config)

def run_makeup_artist() -> str:
    st.title("💄 AI Makeup Artist")

    user_input = st.text_area("Describe your skin type, occasion, or what you want help with:")

    if "makeup_output" not in st.session_state:
        st.session_state.makeup_output = ""

    if st.button("Get Makeup Advice"):
        if user_input:
            with st.spinner("Fetching personalized makeup advice..."):
                try:
                    response = asyncio.run(generate_makeup_advice(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_makeup_advice(user_input))

                st.session_state.makeup_output = response.final_output
        else:
            st.warning("Please describe your need.")

    if st.session_state.makeup_output:
        st.markdown("### ✨ Your Personalized Makeup Advice")
        st.write(st.session_state.makeup_output)
