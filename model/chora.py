import streamlit as st
import os
from openai import OpenAI

#Load the environment variables
from dotenv import load_dotenv
load_dotenv()

#initialize the OpenAI client
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
client = OpenAI()

#create function to get the response from the model
def get_chora_response(user_input: str) -> str:
    chora_chat = client.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:personal:chora:BAYn6u9D",
        messages=[
            {"role": "system", "content": "You are an AI assistant that provides factual and helpful answers about BCHS."},
            {"role": "user", "content": user_input}
        ]
    )
    return chora_chat.choices[0].message.content

#streamlit app
def main():
    st.title("Chora")
    st.write("Welcome to the Chora - Ask me anything about BCHS.")
    user_input = st.text_input("You:")
    if st.button("send"):
        chora_response = get_chora_response(user_input)
        st.write(chora_response)

#when the user submits a messsage get the response from the model
    if user_input:
        with st.spinner("Chora is typing..."):
            chora_response = get_chora_response(user_input)
            st.subheader("Chora's Response:")
            st.write(chora_response)

if __name__ == "__main__":
    main()