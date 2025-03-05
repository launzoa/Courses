from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):
    
    btn = page.get_by_role("link", name="Sample App")
    btn.click()
    
    user = page.get_by_role("textbox", name="User Name")
    password = page.get_by_role("textbox", name="********")
    submit = page.get_by_role("button", name="Log In")
    
    name = "Luã"
    user.fill(name)
    password.fill("pwd")
    submit.click()
    
    result = page.locator("label#loginstatus")
    
    expect(result).to_have_text(f"Welcome, {name}!")    
    

'''
Exemplo simples de um login de usuário, onde fazemos o login e validamos a resposta de bem vindo do website
'''