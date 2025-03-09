from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_click(page: Page):
    
    btn = page.get_by_role("link", name="Click")
    btn.click()

    btn_green = page.get_by_role("button", name="Button That Ignores DOM Click")
    btn_green.click()

    expect(btn_green).to_have_class("btn btn-success")


'''
Sinceramente, não entendi muito o intuito desse teste. Pensei que não era para usar o 'click',
mas ele funcionou perfeitamente... Enfim, está feito
'''