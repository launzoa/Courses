from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    
    page.goto("https://bootswatch.com/default")


def test_app(page: Page):
    
    unchecked = page.get_by_role("checkbox", name="Default checkbox")
    checked = page.get_by_role("checkbox", name="Checked checkbox") 
    
    expect(unchecked).not_to_be_checked() # Como o nome sugere, verifica se o elemento não está checkado
    expect(checked).to_be_checked() # Verifica se o elemento está checkado
    
    