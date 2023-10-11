import streamlit as st

st.title("my practice bot app")
st.write("Lets create a bot app on streamlit")
btn = st.button("Your Name")

if btn:
    st.success('You clicked the button!')

