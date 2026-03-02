from playwright.sync_api import sync_playwright

def fetch_feed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        feed_data = None

        def handle_response(response):
            nonlocal feed_data
            if "/x/feed/f_" in response.url:
                feed_data = response.text()

        page.on("response", handle_response)

        page.goto("https://www.livesport.cz/tenis/", wait_until="networkidle")

        browser.close()

        return feed_data