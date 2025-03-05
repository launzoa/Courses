from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):

    btn = page.get_by_role("link", name="Non-Breaking Space")
    btn.click()
    
    page.locator("//button[text()='My\u00a0Button']").click() #Exemplo feito em XPath
    
    
'''
A conteúdo do nosso elemento está com a seguinte mensagem: "My&nbsp;Button", isso mostra que tem um espaço com
um caractere especial e para nesse caso, é preciso utilizar esse exemplo dado no locator, para conseguir localiza-lo
'''