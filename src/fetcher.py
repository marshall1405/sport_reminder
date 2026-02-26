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

def fetch_match_detail(match_id):
    detail_feed = None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Capture the correct detail feed response
        def handle_response(response):
            nonlocal detail_feed
            if f"/x/feed/ds_{match_id}" in response.url:
                detail_feed = response.text()

        page.on("response", handle_response)

        # Open match page (this triggers detail feed automatically)
        match_url = f"https://www.livesport.cz/zapas/?mid={match_id}"
        page.goto(match_url, wait_until="networkidle")

        browser.close()

    return detail_feed