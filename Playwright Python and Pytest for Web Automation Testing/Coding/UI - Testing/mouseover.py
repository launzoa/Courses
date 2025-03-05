from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):

    btn = page.get_by_role("link", name="Mouse Over")  
    btn.click()
    
    btn_click = page.get_by_title("Click me")
    btn_click.hover()
    
    btn_active = page.get_by_title("Active Link")
    btn_active.click(click_count=2)
    
    result_btn = page.locator("span#clickCount")
    expect(result_btn).to_have_text("2")

    
    btn_link = page.get_by_title("Link Button")
    btn_link.click(click_count=2)
    
    result_link = page.locator("span#clickButtonCount")
    expect(result_link).to_have_text("2")
    
    
'''
Esse teste faz uso de algumas propriedades de clicks, onde ao passar o mouse por cima o elemento pode surgir uma mudança.
Além desse problema, também precisamos fazer uso de dois clicks. Teste simples, onde passamos o mouse por cima do link e caso
suas propriedades mudem, localizamos esse novo elemento e clickamos duas vezes. 
'''