from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_visi(page: Page):

    btn = page.get_by_role("link", name="Visibility")
    btn.click()

    remo = page.get_by_role("button", name="Removed")
    wid = page.get_by_role("button", name="Zero Width")
    over = page.get_by_role("button", name="Overlapped")
    opa = page.get_by_role("button", name="Opacity")
    hid = page.get_by_role("button", name="Visibility Hidden")
    disp = page.get_by_role("button", name="Display None")
    off = page.get_by_role("button", name="Offscreen")


    hide = page.get_by_role("button", name="Hide")
    hide.click()

    
    page.pause()