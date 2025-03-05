from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):

    btn = page.get_by_role("link", name="Overlapped Element")
    btn.click()
    
    inpt = page.get_by_role("textbox", name="Name")
    
    div = inpt.locator("..")
    div.hover()
    
    page.mouse.wheel(0, 200)
    
    name = "Luã"
    inpt.fill(name)
    
    expect(inpt).to_have_value(name)
    
    
'''
Nesse teste, temos um pequeno scroll dentro da div que contem o nosso input. A estratégia, portanto, é acessar o input e 
sair dele utilizando o locator("..") e seleciona-lo. Selecionado, vamos scrollar essa barra para baixo e localizar por
completo o elemento. Adicionar o texto e verificar se o texto está digitado perfeitamente.
'''