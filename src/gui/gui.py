#!/usr/bin/env python3
import streamlit as st
import json
import os

file_path = "./reminder_settings/settings.json"

data = []
if os.path.exists(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
            else:
                data = []
        if not isinstance(data, list):
            data = list(data.values())
    except json.JSONDecodeError:
        data = []
else:
    data = []



settings_tab, data_tab = st.tabs(["Settings", "Data"])

with settings_tab:
    st.title("🏅 Let's setup your personalized SPORT REMINDER 🏅")

    filter_input = st.text_input("Surnames of your favorite Tennis players")
    email_input = st.text_input("Email")

    if st.button("Save Settings"):
        data.append({"filter": filter_input, "email": email_input})
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        st.success("Settings saved!")

with data_tab:
    #st.write(data)

    if data:
        idx = st.number_input("Entry index to edit", min_value=0, max_value=len(data)-1, step=1)
        entry = data[idx]

        st.header(f"Profile: {entry['email']}")

        new_filter = st.text_input("filter", entry["filter"], key=f"filter_{idx}")
        new_email = st.text_input("Email", entry["email"], key=f"email_{idx}")

        if st.button("Update Entry"):
            data[idx] = {"filter": new_filter, "email": new_email}
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            st.success("Entry updated!")
    else:
        st.info("No entries saved yet.")
