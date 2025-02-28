from playwright.sync_api import Page, BrowserContext
import pytest 

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def tracer_example(context: BrowserContext):
    
    context.tracing.start(name="playwright", screenshots=True, snapshots=True, sources=True)
    
    yield 
    
    context.tracing.stop(path="trace.zip")
    
def test_page(page: Page):
    
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="Get started")
    link.click()
    
    assert page.url == DOCS_URL