import streamlit as st

st.title("This website For selecting programming Language")
st.header("Select your favorite programming Language")
Language = st.selectbox("Your Option Are :",["Python","Java","C","C++","Html","Javascript"])
st.write(f"You have selcted {Language} language ")
st.success("You have Selected Your favourite Language")