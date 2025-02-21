from playwright.sync_api import sync_playwright
from decks import EMAIL, PASSWORD, PATH

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    
    # Cria um novo contexto de navegação. Um contexto é um ambiente isolado que armazena cookies, cache e outras informações.
    context = browser.new_context()
    
    # Abre uma nova página no contexto criado.
    page = context.new_page()
    page.goto("https://accounts.google.com")
    
    inpt_email = page.locator("input#identifierId")
    inpt_email.fill(EMAIL)

    page.locator("div#identifierNext").click()
    
    inpt_password = page.get_by_label("Digite sua senha")
    inpt_password.fill(PASSWORD)
    
    page.locator("div#passwordNext").click()
    
    page.pause()
    
    # Salva o estado de autenticação (cookies, localStorage, etc.) em um arquivo JSON, esse arquivo pode ser carregado posteriormente para reutilizar a sessão autenticada.
    context.storage_state(
        path=PATH
    )
    context.close()
    
    page.close()
    
    '''
    Esse código é a base para criar um autenticador de email, nesse programa estamos autenticando com determinado email salvo em decks e utilizamos o contextque é uma forma de conseguir
    salvar essa sessão, após o email ser autenticado, em um bloco de cookies para podermos acessá-lo novamente sem precisar inserir os dados novamente em outro programa.
    '''
    