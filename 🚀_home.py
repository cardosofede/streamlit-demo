import streamlit as st

app_title = "Streamlit Tutorial"

st.set_page_config(page_title=app_title, page_icon="🦅", layout="wide")

st.title("My first App!")
st.write("---")

is_easy = st.checkbox('Streamlit is easy!')
animal = st.radio('Pick one', ['cats', 'dogs'])
name = st.text_input('First name')
button = st.button('Click me')

if button:
    st.write(f"The name is {name}, and the animal is {animal}.")
    if is_easy:
        st.write("For the user Streamlit is easy")

st.sidebar.write("---")
st.sidebar.text_input("My first text input in the sidebar")