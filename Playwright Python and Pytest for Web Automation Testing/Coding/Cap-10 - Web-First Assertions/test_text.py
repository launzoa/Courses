from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    
    page.goto("https://playwright.dev/python")
    

def test_texts(page: Page):
    
    
    heading = page.get_by_role("heading", name="Playwright enables reliable")
    
    expect(heading).to_contain_text("Playwright") # tc_Text, verifica se o nosso conteúdo está presente em determinado elemento
    
    expect(heading).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.") #th_Text, verifica se o conteúdo é exatamente igual ao presente no elemento
    
    
    
   