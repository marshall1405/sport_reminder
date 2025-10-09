import streamlit as st

st.title("🏅 Let's setup your personalized SPORT REMINDER 🏅")

sport = st.text_input("Sport")
email = st.text_input("Email")
time = st.text_input("Reminder Time")

if st.button("Save Settings"):
    st.success(f"Reminder set for {sport} at {time}\nEmail: {email}")
