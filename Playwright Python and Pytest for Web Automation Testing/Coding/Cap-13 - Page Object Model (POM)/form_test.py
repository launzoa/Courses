from playwright.sync_api import Page, expect
import pytest
from form_class import Form


def test_sucess(page: Page):
    
    name = "Luã"
    password = "pwd"

    login_page = Form(page)
    
    login_page.login(name, password)

    expect(login_page.resul).to_have_text(f"Welcome, {name}!")    
    

def test_fail(page: Page):
    
    name = "Luã"
    password = "sla"

    login_page = Form(page)
    
    login_page.login(name, password)

    expect(login_page.resul).to_have_text("Invalid username/password")    
    



'''
Exemplo simples de um login de usuário, onde fazemos o login e validamos a resposta de bem vindo
do website utilizando um sistema mais robusto com classe externa para realizar as nossas funções
e essa página para realizar determinados testes e validações.
'''