import streamlit as st

st.title("🤖 AI Assistant")

st.write("Ask any cricket-related question")

user_question = st.text_input("Write your query")

if user_question:
    question = user_question.lower()

    if "virat" in question :
        st.success(    "Virat Kohli is known for his consistency, strong cover drives, "
            "and excellent chasing ability, especially in ODIs.")
        
    elif "dhoni" in question :
        st.success(
            "MS Dhoni is famous for his calm captaincy, helicopter shot,"
            "and finishing skills under pressure."
            )

    elif "best batsman" in question:
        st.success(
        
        "   The best batsman depends on format. "
            "Virat Kohli excels in ODIs, "
            "Babar Azam is strong in modern formats, "
            "and Joe Root dominates Tests."
        )

    elif "bowling" in question:
        st.success(
            "Good bowling requires line, length, variation, and reading the batsman."
        )

    else:
        st.warning(
            "I am still learning 🤖. Try asking about a famous player or batting skills."
        )