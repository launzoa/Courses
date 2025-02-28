from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_screen(page: Page):
    
    page.goto("https://playwright.dev/python")
    
    page.screenshot(path="Image/screen_home.jpg")
    
    link = page.get_by_role("link", name="Get started")
    link.click()
    
    page.screenshot(path="Image/screen_docs.jpg")

    assert page.url == DOCS_URL