from playwright.sync_api import sync_playwright

def open_spotify():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://open.spotify.com/")

        page.wait_for_timeout(5000)

        print("Spotify opened successfully")

        browser.close()


