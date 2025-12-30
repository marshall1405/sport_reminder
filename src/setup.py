import os
import sys
from sender import send_emails_from_settings
from fetcher import fetch_html_text
from html_parser import create_matches_leagues, parse_leagues, parse_matches

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
        # for now we will use this tennis url
        url = "https://www.livesport.cz/tenis/"

        html = fetch_html_text(url)
        matches, leagues = create_matches_leagues(html)

        #p_leagues = parse_leagues(leagues, html)
        p_matches = parse_matches(matches, leagues, html)

        send_emails_from_settings("Dnesni Tenisove Zapasy", p_matches)    


    elif choice == "4":
        sys.exit()

    else:
        print("Unrecognized Input")
        setup_menu()

