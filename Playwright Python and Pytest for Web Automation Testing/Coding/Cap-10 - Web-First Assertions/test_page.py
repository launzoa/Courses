from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("https://playwright.dev/python")


def test_url(page: Page):
    
    print(page.url)
    
    btn_docs = page.get_by_role("link", name="Get started")
    btn_docs.click()
    
    print(page.url)
    
    expect(page).to_have_url("https://playwright.dev/python/docs/intro") # th_Url, verifica se a url da página é a mesma da que estamos passando
    expect(page).to_have_title("Installation | Playwright Python") # th_Title, verifica o título da página e compara com o que estamos passando