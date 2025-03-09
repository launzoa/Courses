from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_layer(page: Page):
    
    btn = page.get_by_role("link", name="Hidden Layers")
    btn.click()

    btn_green = page.locator("button#greenButton")
    expect(btn_green).to_be_visible()
    btn_green.click()

    btn_blue = page.locator("button#blueButton")
    expect(btn_blue).to_be_visible()
    btn_blue.click()

'''
Esse teste é para verificar a ação invísivel de alguns elementos. Nesse caso em específico,
temos um botão que ao ser clickado, é criado um novo elemento no mesmo lugar do antigo botão
Para resolver, é preciso executar o teste e guardar dois ids diferentes, um para cada botão
'''