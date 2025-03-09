from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_attr(page: Page):
    
    btn_page = page.get_by_role("link", name="Class Attribute")
    btn_page.click()

    btn_primary = page.locator("button.btn-primary")
    btn_primary.click()

    expect(btn_primary).to_be_visible()
    

'''
Nesse teste, temos que atráves do css_selector ou xpath, encontrar o botão da cor azul
O detalhe desse teste é que ao recarregar a página, os botões trocam de lugar entre si.
Para passar nesse teste, tive que detectar o locator desse botão azul, que é denotado por
conter a classe 'btn-primary'. Apesar de ter outras classes que mudam entre si, essa se mantém ao elemento.
'''