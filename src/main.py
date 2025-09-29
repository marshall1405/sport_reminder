from fetcher import fetch_html_text
from html_parser import create_matches_leagues,parse_matches, parse_leagues
from message_formatter import format_matches_html
from sender import send_email
from filter import filter_players, filter_tournaments, filter_all, create_player_array, create_tournament_array


player_filter = input("Enter the SURNAME of a PLAYER you like: ")
tournament_filter = input("Enter the name of a TOURNAMENT you like: ")

players = create_player_array(player_filter)
tournaments = create_tournament_array(tournament_filter)

# for now we will use this tennis url
url = "https://www.livesport.cz/tenis/"

html = fetch_html_text(url)
matches, leagues = create_matches_leagues(html)

parse_leagues(leagues, html)
parse_matches(matches, leagues, html)

filtered_matches = filter_all(matches, players, tournaments)

html = format_matches_html(filtered_matches)

send_email("Dnesni Tenisove Zapasy", html)





