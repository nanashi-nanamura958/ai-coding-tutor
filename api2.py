import streamlit as st
import requests

# App title and description
st.title("🤖 AI Coding Tutor")
st.write("Enter a coding problem below. The AI will solve it and explain it to you.")

# Sidebar for API key and settings
with st.sidebar:
    st.header("Settings")
    together_api_key = st.text_input("Enter your Together AI API key", type="password")
    model = st.selectbox("Select model", [
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "meta-llama/Llama-2-13b-chat-hf",
        "meta-llama/Llama-2-70b-chat-hf",
        "teknium/OpenHermes-2.5-Mistral-7B"
    ], index=0)
    temp = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7, 0.1)

    st.markdown("---")
    st.markdown("""
    **How to use:**
    1. Enter your Together AI API key  
    2. Type your coding problem  
    3. Click 'Get Solution'
    """)

# Text area for user to enter the coding problem
problem = st.text_area(
    "Your coding problem",
    placeholder="e.g. Find the longest palindromic substring in a string.",
    height=150
)

# Additional options
col1, col2 = st.columns(2)
with col1:
    language = st.selectbox(
        "Programming language",
        ["Python", "JavaScript", "Java", "C++", "Go"],
        index=0
    )
with col2:
    difficulty = st.selectbox(
        "Explanation level",
        ["Beginner", "Intermediate", "Advanced"],
        index=0
    )

# When user clicks the button
if st.button("Get Solution", type="primary"):
    if not together_api_key:
        st.error("🚨 Please enter your Together AI API key!")
    elif not problem.strip():
        st.error("🚨 Please enter a coding problem!")
    else:
        with st.spinner("Analyzing the problem and crafting a solution..."):
            headers = {
                "Authorization": f"Bearer {together_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": f"You are a helpful {language} coding tutor."},
                    {"role": "user", "content": f"""
You are an expert {language} coding tutor specialized in teaching {difficulty.lower()} programmers.
Given this problem: {problem}
Please provide:
1. An efficient solution in {language}, formatted with proper indentation (use markdown-style code block: ```{language} ... ```).
2. A step-by-step explanation in {difficulty}-friendly language.
3. A diagram or ASCII illustration to help visualize the algorithm (especially the partitioning logic if applicable).
4. Time and space complexity analysis.
5. Example input and output.
6. Edge cases to consider.

"""}
                ],
                "temperature": temp
            }

            try:
                response = requests.post(
                    "https://api.together.xyz/v1/chat/completions",
                    headers=headers,
                    json=payload
                )
                if response.status_code == 200:
                    data = response.json()
                    answer = data["choices"][0]["message"]["content"]

                    with st.expander("See Solution", expanded=True):
                        st.markdown(answer)

                    if "usage" in data:
                        usage = data["usage"]
                        st.info(f"Tokens used: {usage['total_tokens']} "
                                f"(Prompt: {usage['prompt_tokens']}, "
                                f"Completion: {usage['completion_tokens']})")
                else:
                    st.error(f"❌ API Error {response.status_code}: {response.text}")

            except Exception as e:
                st.error(f"⚠️ Unexpected error: {e}")

