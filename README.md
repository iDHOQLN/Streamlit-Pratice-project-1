# Streamlit-Pratice-project-1
Pratice


import streamlit as st

def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # This is a placeholder for actual authentication logic
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
            # Here you would typically store login status in session state
            # and redirect to another page or show different content.
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    # You can add session state management here to show different content
    # based on whether the user is logged in.
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login_page()
    else:
        st.write(f"Welcome, {st.session_state['username']}!")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()
