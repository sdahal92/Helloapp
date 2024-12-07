import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("This is your first Streamlit app. Feel free to customize it!")

# Add a sample input and output
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")

