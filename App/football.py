import streamlit.elements.lib.image_utils
import streamlit as st


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "users" not in st.session_state:
    st.session_state["users"] = {'admin':'admin'}

def LoginpageI():
    st.title("Login Page")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        col1,col2 = st.columns(2)
        with col1:
            submit_login = st.form_submit_button("Login")
          
        with col2:
            submit_create = st.form_submit_button("Create Account")

    if submit_login:
        if username in st.session_state ["users"] and st.session_state['users'][username]== password:
            st.switch_page("pages/Audio_page.py")
            
            st.session_state["navigation_bar"] = "pages/Audio_page.py"
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome back,{username}")
            
            
        else:
            st.error("Invalid username or password : Click on Create Account")
    if submit_create:
        if username == "" and password =="" :
          st.error("Username Cannot be empty")
        elif username in st.session_state['users']:
         st.error("Username and password Already Exists")
        else :
            st.session_state['users'][username] = password
            st.success(f"Account of {username} Created Successfully : You Can Loggin it ")
            
LoginpageI()

st.logo(
    "https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
    link="https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
    icon_image="https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
)




        

