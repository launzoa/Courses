from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("http://uitestingplayground.com")


def test_tables(page: Page):

    btn = page.get_by_role("link", name="Dynamic Table")
    btn.click()

    table = page.get_by_role("rowgroup")

    col = table.locator("nth=0").locator("span")
    
    i = 0
    while(col.locator(f"nth={i}").inner_html() != "CPU"):
        i += 1 

    col_value = i
    
    lin = table.locator("nth=1").locator("div")

    for i in range(0,4):
        if lin.locator(f"nth={i}").locator("span").locator("nth=0").inner_html() == "Chrome":
            porcentage = lin.locator(f"nth={i}").locator("span").locator(f"nth={col_value}").inner_html()


    assert(porcentage) in page.locator("p.bg-warning").inner_html()


'''
Esse teste consiste em pegar uma tabela dinâmica, logo, que muda os valores da coluna entre si e das linhas entre si.
É fornecido a porcentagem de uso da CPU para carregar a página, o objetivo do teste é pegar essa porcentagem dada e comparar
com a porcentagem da tabela do nosso respectivo browser. No caso do teste foi o Chrome.
Um teste simples, porém levemente confuso no começo para manipular os elementos e seus parentescos, mas com erros e acertos
foi possível conseguir chegar em um resultado agradável.
'''