from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("https://bootswatch.com/default")


def test_menu(page: Page):
    
    select = page.get_by_label("Example select")
    multi_select = page.get_by_label("Example multiple select")
    multi_select.select_option(["1", "2"]) # Marca dois valores no select
    
    expect(select).to_have_value("1") # Verifica se um valor está presente no elemento
    
    expect(multi_select).to_have_values(["1", "2"]) # Verifica se dois ou mais valores estão presentes