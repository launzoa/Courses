from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    
    page.goto("https://playwright.dev/python")


def test_element(page: Page):
    
    btn1 = page.get_by_role("button", name="Python")
    expect(btn1).to_be_visible() # Visible, serve para determinar se um elemento está vísivel na página (como o nome sugere)
    expect(btn1).to_be_enabled() # Enabled, no caso de algum elemento interativo pode ser clickado ou preenchido
    
    
    btn2 = page.get_by_role("link", name="Node.js")
    expect(btn2).to_be_hidden() # Hidden, funciona caso um elemento esteja oculto dentro da página, pode estar no DOM, mas não vísivel
    
    expect(btn2).not_to_be_visible() # ntb_Visible, é similar ao hidden, porém, aqui o elemento pode estar no DOM ou não
    
    
    