from playwright.sync_api import Page, expect
import pytest, re


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):

    btn = page.get_by_role("link", name="Visibility")
    btn.click()

    remo = page.get_by_role("button", name="Removed")
    wid = page.get_by_role("button", name="Zero Width")
    over = page.get_by_role("button", name="Overlapped").locator("..")
    opa = page.get_by_role("button", name="Opacity 0")
    hid = page.get_by_role("button", name="Visibility Hidden")
    disp = page.get_by_role("button", name="Display None")
    off = page.get_by_role("button", name="Offscreen")


    hide = page.get_by_role("button", name="Hide")
    hide.click()
    
    expect(remo).to_be_hidden()
    expect(wid).to_have_class(re.compile(r"zerowidth"))
    expect(over.locator("div")).to_have_id("hidingLayer")
    expect(opa).to_have_css("opacity", "0")
    expect(hid).to_be_hidden()
    expect(disp).to_be_hidden()    
    expect(off).not_to_be_in_viewport()

'''
Esse exercício se consiste em testar algumas propriedades que deixam
determinados elementos, invísiveis ao seu jeito.
'''
