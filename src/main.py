from fetcher import fetch_html_text
from html_parser import parse_whole_page
# for now we will use this tennis url
url = "https://www.livesport.cz/tenis/"

html = fetch_html_text(url)
indices = parse_whole_page(html)

for i in indices:
    print(html[i:i+100])


with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("File saved successfully!")

