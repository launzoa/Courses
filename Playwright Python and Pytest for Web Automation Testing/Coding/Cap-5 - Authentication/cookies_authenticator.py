from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    
    # Cria um novo contexto de navegação, carregando o estado de armazenamento (cookies) a partir do arquivo 'storage_state.json'. 
    context = browser.new_context(
        storage_state="storage_state.json"
    )
    
    page = context.new_page()
    page.goto("https://accounts.google.com")
    
    page.pause()

    context.close()
    
    page.close()
    
'''
Nesse codigo, utilizamos os cookies do programa authenticator e entramos no email sem precisar ter que inserir os dados, porque já fizemos isso uma vez e salvamos esse dados como forma de cookie
dentro do 'storage_state.json'. Após os dados salvos, apenas chamamos esses cookies para conectar automaticamente no servidor do email.
'''
    