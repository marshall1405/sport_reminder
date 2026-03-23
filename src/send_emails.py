from filter import filter_players, normalize_players, load_settings
from parser import map_feed_to_objects, extract_all_matches
from fetcher import fetch_feed
from message_formatter import format_matches_html
from sender import send_email

leagues = map_feed_to_objects(fetch_feed())
matches = extract_all_matches(leagues)

settings = load_settings()

for user in settings:
    email = user.get("email")
    players = normalize_players(user.get("filter"))
    user_matches = filter_players(matches, players)

    if not user_matches:
        continue

    html = format_matches_html(user_matches)
    send_email("Dnešní Tenisové Zápasy", html, email)
    print(f"Sent email to {email}")
