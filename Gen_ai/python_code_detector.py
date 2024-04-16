import streamlit as st
from openai import OpenAI

# Read API key from file
with open(".openai_api_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title with emojis
st.title("🤖 Python Code Review with OpenAI 🧐")

# User input section with styled header and emoji
st.header("🔥 Enter Your Python Code 🔥")

prompt = st.text_area("Enter your Python code here:", height=100)

# Button to trigger code review with emoji
if st.button("Review the Code 🚀"):
    st.markdown("<h2 style='color:gray;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    st.write(generated_text)
