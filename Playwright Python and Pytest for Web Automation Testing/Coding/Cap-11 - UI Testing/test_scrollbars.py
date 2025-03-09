from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_scroll(page: Page):
    
    btn = page.get_by_role("link", name="Scrollbars")
    btn.click()

    btn_sucess = page.get_by_role("button", name="Hiding Button")
    btn_sucess.scroll_into_view_if_needed()
    btn_sucess.click()
    
    expect(btn_sucess).to_be_visible()


'''
Esse teste tem um botão escondido dentro de uma caixa de scroll. O intuito é encontrar esse
botão dentro dessa caixa utilizando algumas técnicas de scroll.
Felizmente, tem o 'scroll_into_view_if_needed', onde caso eu precise, ele encontra o elemento
dentro da caixa de scroll, scrollando se preciso
'''