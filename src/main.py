from fetcher import fetch_html_text
from html_parser import create_matches_leagues,parse_matches, parse_leagues
from message_formatter import format_matches_html
from sender import send_email


player_filter = input("Enter the SURNAME of a PLAYER you like: ")
tournament_filter = input("Enter the name of a TOURNAMENT you like: ")

# for now we will use this tennis url
url = "https://www.livesport.cz/tenis/"

html = fetch_html_text(url)
matches, leagues = create_matches_leagues(html)

parse_leagues(leagues, html)
parse_matches(matches, leagues, html)

single_future_matches = [m for m in matches if m.time != "No Time" and m.league.single]
future_matches = [m for m in matches if m.time != "No Time"]

html = format_matches_html(future_matches)

send_email("Dnesni Tenisove Zapasy", html)





