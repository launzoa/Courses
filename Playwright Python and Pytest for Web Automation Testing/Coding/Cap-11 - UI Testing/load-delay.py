from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_load(page: Page):
    
    btn = page.get_by_role("link", name="Load Delay")
    btn.click()
   
    btn_sucess = page.get_by_role("button", name="Button Appearing After Delay")
    btn_sucess.wait_for()
    
    expect(btn_sucess).to_be_visible()


'''
Alguns servidores podem demorar mais do que o esperado. Nesse teste é realizado uma 'espera'
até que a página seja carregada.
O 'wait_for', nos cabe muito bem nesse caso para esperar para realizar uma ação
'''