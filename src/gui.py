import streamlit as st
import json 

st.title("🏅 Let's setup your personalized SPORT REMINDER 🏅")

filter = st.text_input("Surnames of your favorite Tennis players")
email = st.text_input("Email")

if st.button("Save Settings"):
    with open("./reminder_settings/settings.json", "a") as f:
        json.dump({"filter": filter, "email": email}, f, ensure_ascii=False)
    st.success("Settings saved!")
