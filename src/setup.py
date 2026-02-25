import os
import sys
from filter import filter_players, normalize_players, load_settings
from parser import map_feed_to_objects, extract_all_matches
from fetcher import fetch_feed
from message_formatter import format_matches_html
from sender import send_email

def setup_menu():
    print("SPORT REMINDER SETUP")
    print("1: Open Streamlit GUI")
    print("2: Schedule daily on Raspberry Pi (cron)")
    print("3: Send Mail to configured participants")
    print("4: Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        os.system("streamlit run ./gui/gui.py")
    
    elif choice == "2":
        print("Setting stuff up")
        #TODO Cron

    elif choice == "3":
        leagues = map_feed_to_objects(fetch_feed())
        matches = extract_all_matches(leagues)

        settings = load_settings()

        for user in settings:
            players = normalize_players(user.get("filter"))
            email = user.get("email")

            user_matches = filter_players(matches, players)

            if user_matches:
                html = format_matches_html(user_matches)
                send_email(
                    subject="Dnešní Tenisové Zápasy",
                    message=html,
                    to=email
                )


    elif choice == "4":
        sys.exit()

    else:
        print("Unrecognized Input")
        setup_menu()

