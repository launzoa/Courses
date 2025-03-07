from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_bar(page: Page):

    btn = page.get_by_role("link", name="Progress Bar")
    btn.click()

    bar = page.locator("div#progressBar")
    
    start = page.get_by_role("button", name="Start")
    start.click()
    stop = page.get_by_role("button", name="Stop")


    while True:
        porcentage = int(bar.get_attribute("aria-valuenow"))

        if porcentage >= 75:
            stop.click()
            break


    assert(porcentage) >= 75
    

'''
Esse problema nos mostra uma barra de progresso que vai crescendo e precisamos para-la quando a mesma atingir acima de 
75%. Um teste que faz uso de laços loop para conseguir detectar quando chegar nesse valor e conseguir para-lo
'''