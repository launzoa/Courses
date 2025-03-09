from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_dynamic_id(page: Page):
    btn_page = page.get_by_role("link", name="Dynamic ID")
    btn_page.click()

    btn_id = page.locator("button.btn.btn-primary")
    btn_id.click()

    expect(btn_id).to_be_visible()


'''
Esse teste pede que a gente aprenda a detectar os elementos sem se apegar ao seu ID, afinal
nesse caso, o id é dinâmico, então ao recarregar a página, o id muda de nome. Para realizar esse 
teste foi preciso detectar a classe usando do elemento usando o css_selector. 
'''