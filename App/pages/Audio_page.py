from streamlit import container
import streamlit as st


with st.popover("open Pop Over"):
    st.markdown("Welcome To Audio Page")

container = st.container(border=True)

container.title("Audio Page")
container.write("Welcome to the Audio Page")

st.logo(
    "https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
    link="https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
    icon_image="https://img.freepik.com/free-vector/moon-with-stars_98292-1046.jpg?semt=ais_hybrid&w=740&q=80",
)
st.write("Listen A SONG")
audio_file_path = "App/audio_file/music4.mp3"  
try:
    with open(audio_file_path, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
except FileNotFoundError:
    st.error(f"Audio file not found at: {audio_file_path}")

st.write("Fifa Draw 2026")
st.write("Football")

if st.button("Logout"):
        st.switch_page("football.py")
        st.session_state['logged_in'] = False
        st.session_state.pop('username', None) 
        st.success("You have been logged out.")
        