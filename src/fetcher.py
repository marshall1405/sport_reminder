from playwright.sync_api import sync_playwright

def fetch_html_text(url):
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="networkidle")

        html = page.content()

        browser.close()
    return html

