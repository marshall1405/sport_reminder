from fetcher import fetch_html_text
from html_parser import create_matches_leagues,parse_matches, parse_leagues
# for now we will use this tennis url
url = "https://www.livesport.cz/tenis/"

html = fetch_html_text(url)
matches, leagues = create_matches_leagues(html)

parse_leagues(leagues, html)
parse_matches(matches, leagues, html)

for m in matches:
    m.print()



