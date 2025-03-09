from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def visit_page(page: Page):

    page.goto("http://www.uitestingplayground.com/")


def test_input(page: Page):
    
    btn = page.get_by_role("link", name="Text Input")
    btn.click()

    inpt = page.get_by_role("textbox", name="Set New Button Name")
    text = "Novo texto para o botão"
    inpt.fill(text)

    btn_sucess = page.get_by_role("button", name="Button That Should Change it's Name Based on Input Value")
    btn_sucess.click()

    btn_sucess_1 = page.locator("button#updatingButton")
    btn_sucess_2 = page.get_by_role("button", name=text)

    expect(btn_sucess_1).to_be_visible()
    expect(btn_sucess_2).to_be_visible()

'''
Esse teste ele nos apresenta um input para colocar o texto e ao clickar no botão com o novo
texto inserido, o nome do botão muda para o texto.
Fiz duas respostas, uma que utiliza o id do botão (cujo o qual não muda) e outra que utilizo o 
próprio texto inserido no input (mas esse é um caso a parte, já que eu sei o texto inserido), porém,
poderia ser feito após o input, um text() para pegar o texto do elemento e afins...
'''
