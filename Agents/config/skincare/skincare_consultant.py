# skincare_consultant.py
from config.sdk_client import model, config
from agents import Agent, Runner
import streamlit as st
import asyncio

skincare_agent = Agent(
    name="Skincare Consultant",
    instructions="You are a certified skincare consultant. Give personalized skincare routines and product suggestions based on skin type and concerns.",
    model=model
)

async def generate_skincare_advice(user_input: str):
    return await Runner.run(skincare_agent, user_input, run_config=config)

def run_skincare_consultant():
    st.title("🧴 AI Skincare Consultant")
    user_input = st.text_area("Tell me your skin type or any issues you're facing:")

    if "skincare_output" not in st.session_state:
        st.session_state.skincare_output = ""

    if st.button("Get Skincare Tips"):
        if user_input:
            with st.spinner("Analyzing your skincare needs..."):
                try:
                    response = asyncio.run(generate_skincare_advice(user_input))
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    response = loop.run_until_complete(generate_skincare_advice(user_input))

                st.session_state.skincare_output = response.final_output
        else:
            st.warning("Please describe your concern.")

    if st.session_state.skincare_output:
        st.markdown("### 🌿 Skincare Advice")
        st.write(st.session_state.skincare_output)

