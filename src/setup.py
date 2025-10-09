import os
import sys

def setup_menu():
    print("SPORT REMINDER SETUP")
    print("1: Open Streamlit GUI")
    print("2: Schedule daily on Raspberry Pi (cron)")
    print("3: Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        os.system("streamlit run ./gui/gui.py")
    
    elif choice == "2":
        print("Setting stuff up")
        #TODO Cron

    elif choice == "3":
        sys.exit()

    else:
        print("Unrecognized Input")
        setup_menu()

