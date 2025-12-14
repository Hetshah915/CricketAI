import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

st.title("🤖 AI Assistant")
st.write("Ask any cricket-related question")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def rule_based_question(question):
    if "virat" in question:
        return "Virat Kohli is known for consistency and strong chasing ability."
    if "dhoni" in question:
        return "MS Dhoni is famous for calm captaincy and finishing skills."
    return None

user_question = st.text_input("Write your query")

if user_question:
    question = user_question.lower()

    rule_answer = rule_based_question(question)

    if rule_answer:
        st.success(rule_answer)
    else:
        with st.spinner("AI is thinking ⏳"):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful cricket expert."},
                    {"role": "user", "content": user_question}
                ]
            )

        st.success(response.choices[0].message.content)

         
                                           
                                  
                                           
                                           
                                           

