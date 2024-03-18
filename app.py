import streamlit as st
from lllm_helper import generate_response

st.title("Grey's Summary Generator")

# character = st.text_input(
#     "Enter character name:",
#     placeholder='Meredith Grey',
# )

character = st.selectbox(
    "Select Character:",
    (
        "Meredith Grey",
        "Cristina Yang",
        "George O'Malley",
        "Alex Karev",
        "Lexie Grey",
        "Derek Shepperd",
        "Addison Montgomery",
        "Owen Hunt",
    ),
)

generate = st.button(
    "Generate",
    type="primary",
)

if character and generate:
    response = generate_response(character)
    st.write(response["char_summary"])
