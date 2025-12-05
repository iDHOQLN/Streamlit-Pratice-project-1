import streamlit as st

st.title("Welcome To My First Website")
st.header("Hello World")
st.subheader("This is a Subheader")
st.write("choose he who is goat of football")
goat = st.selectbox("Your Option Are : ", ["Lionel Messi", "Cristiano Ronaldo", "Mbappe", "neymar"])
st.write(f"choose he who is {goat}. of football")
st.success("You have selected the goat of football")