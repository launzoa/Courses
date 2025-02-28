from playwright.sync_api import Page, Browser
import pytest

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture
def recordable_page(browser: Browser):
    
    context = browser.new_context(record_video_dir="video/")
    page = context.new_page()
    yield page
    context.close()

def test_record(recordable_page: Page):

    
    recordable_page.goto("https://playwright.dev/python")
    
    link = recordable_page.get_by_role("link", name="Get started")
    link.click()
    
    assert recordable_page.url == DOCS_URL