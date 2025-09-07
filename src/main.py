from fetcher import fetch_html_text
from html_parser import create_matches
# for now we will use this tennis url
url = "https://www.livesport.cz/tenis/"

html = fetch_html_text(url)
matches = create_matches(html)

for m in matches:
    m.print()



