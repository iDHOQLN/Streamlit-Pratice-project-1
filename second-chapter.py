import streamlit as st

st.title("welcome To chai making")

if st.button("make Chai"):
    st.success("Chai is Ready")

add_masala = st.checkbox("Add masala")

if add_masala:
    st.success("Masala Added")

tea_type = st.radio("Select the base of tea : " ,["milk","Almond Milk","Water"])
st.write(f"selected Base is {tea_type}")

flavour = st.selectbox("Select The flavour of tea :" , ["Adrak" , "Kesar" , "tulshi"])
st.write(f"selected flavour is  {flavour}")

Sugar = st.slider("Select The Sugar quentatiy" , 0,1,6)
st.write(f"Selected Sugar Quantity is {Sugar}")

Cups = st.number_input("How many cups" , min_value = 1,max_value = 10,value = 1)
st.write(f"Selected Number of Cups is {Cups}")

name = st.text_input("Enter Your Name")

if name : 
    st.write(f"welcome {name} ! Your Order Is On The Way")

dob = st.date_input("Enter Your Date of Birth")
st.write(f"Your Date of Birth is {dob}")
