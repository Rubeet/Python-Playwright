from playwright.sync_api import sync_playwright
import os


def get_playwright_instance(user_data_path=None):
    playwright = sync_playwright().start()

    # For normal window without incognito
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, 'Google\\Chrome\\User Data\\Default')
    context = playwright.chromium.launch_persistent_context(user_data_path, headless=False)

    # For incognito window
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    return context
