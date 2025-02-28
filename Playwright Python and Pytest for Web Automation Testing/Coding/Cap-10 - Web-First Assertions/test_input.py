from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    
    page.goto("https://playwright.dev/python")


def test_inpt(page: Page):
    
    input = page.get_by_role("searchbox", name="Search")
    expect(input).to_be_hidden() # Verifica se o elemento está invisível na página
    
    press_input = page.get_by_role("button", name="Search (Ctrl+K)")
    press_input.press("Control+KeyK") # Gera a ação de comandos do teclado
    expect(input).to_be_visible() # Verifica se o elemento está vísivel
    expect(input).to_be_empty() # Verifica se o elemento está vázio

    input.fill("Assertions")
    
    expect(input).to_have_value("Assertions") # Verifica se o valor está presente no elemento

