import streamlit as st

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'users' not in st.session_state:
    st.session_state['users'] = {'admin': 'admin'}

def login_page():
    st.title("Login Page")
 
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    
        col1, col2 = st.columns(2)
        with col1:
            submit_login = st.form_submit_button("Login")
        with col2:
            submit_create = st.form_submit_button("Create Account")
        
        if submit_login:
            if username in st.session_state["users"] and st.session_state["users"][username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"Welcome back, {username}!")
               
            else:
                st.error("Invalid username or password.")
        
        if submit_create:
            if username == "" or password == "":
                st.error("Username and password cannot be empty.")
            elif username in st.session_state['users']:
                st.error("Username already exists. Please choose a different one.")
            else:
                st.session_state['users'][username] = password
                st.success(f"Account for '{username}' created successfully! You can now log in.")

    
def football_info_page():

    st.title(f"Welcome, {st.session_state.get('username', 'User')}! Your Football Hub")
    st.write(f"Welcome, {st.session_state.get('username', 'User')}! Your Football Hub")

    st.header("Latest Football News ⚽")
    st.markdown("""
    **Headline 1**: [Team A] Clinches League Title in Thrilling Finale!
    *   Summary: After a nail-biting season, [Team A] secured the championship with a decisive win on the final day.
    """)
    st.markdown("""
    **Headline 2**: Transfer Rumour: Star Striker [Player Name] Linked to [Big Club]
    *   Summary: Reports suggest that [Player Name] is on the verge of a record-breaking transfer to [Big Club] in the summer window.
    """)

    st.header("Upcoming Matches")
    st.table({
        "Date": ["2023-10-27", "2023-10-28", "2023-10-28"],
        "Match": ["Real Madrid vs Barcelona", "Man Utd vs Liverpool", "Bayern Munich vs Dortmund"],
        "Competition": ["La Liga", "Premier League", "Bundesliga"]
    })

    st.header("Player Spotlight: Kylian Mbappé")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Kylian_Mbapp%C3%A9_2018.jpg/220px-Kylian_Mbapp%C3%A9_2018.jpg", caption="Kylian Mbappé", width=200)
    st.write("""
    Kylian Mbappé is a French professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and captains the France national team.
    Known for his dribbling, explosive speed, and clinical finishing, Mbappé is widely regarded as one of the best players in the world.
    """)

    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state.pop('username', None) # Remove username from session state
        st.success("You have been logged out.")
        st.experimental_rerun() # Rerun to go back to login page

# Main application logic
if st.session_state['logged_in']:
    football_info_page()
else:
    login_page()

