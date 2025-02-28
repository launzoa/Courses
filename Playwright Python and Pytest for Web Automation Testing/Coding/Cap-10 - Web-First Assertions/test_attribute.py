from playwright.sync_api import Page, expect
import pytest, re

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    
    page.goto("https://playwright.dev/python")


def test_attr(page: Page):
    
    head = page.get_by_role("heading", name="Playwright enables reliable")
    nav = page.get_by_role("navigation", name="Main")
    
    expect(head).to_have_class("hero__title heroTitle_ohkl") # Verifica se possui exatamente essa classe como sendo a classe do elemento
    
    expect(nav).to_have_class(re.compile(r"navbar")) # Com o re.compile, ele nos permite verificar se a classe está inclusa dentro do elemento e não necessariamente se é totalmente exata a classe
    
    expect(nav).to_have_attribute("aria-label", "Main") # Verifica se o atributo e o valor estão presentes dentro do elemento
    

    
