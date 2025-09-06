import requests

def fetch(url):
    html = requests.get(url)
    if html.status_code == 200:
        return html.text[:]
    else:
        return "Something Went Wrong: " + html.status_code