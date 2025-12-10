import streamlit as st

st.title("Welcome To Chai Vote Poll")

col1,col2 = st.columns(2)

with col1:
    st.header("Masala chai")
    vote1 = st.button("Vote for Masala Chai")
    st.image("https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai-Featured.jpg" , width=100)

with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote for Adrak Chai")
    st.image("https://budleaf.com/wp-content/uploads/2023/08/Adrak-masala-chai-scaled.jpeg" , width=200)

if vote1 :
    st.success("You Selected Masala Chai")
elif vote2:
    st.success("You Selected Adrak Chai")

name = st.sidebar.text_input("Enter Your Name")
tea =   st.sidebar.selectbox("Select Your Tea", ["Masala Chai", "Adrak Chai"])


st.write(f"Welcome To  {name} and you selected {tea}")