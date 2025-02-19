from playwright.sync_api import sync_playwright # Biblioteca base
 
with sync_playwright() as playwright: # Abrir o playwright de forma síncrona e com o operador with
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge") # Definir as características do nosso browser, headless é para ser vísivel a aba, slow_mo o tempo de cada ação e channel o nosso browser, nesse caso utilizei o edge
    
    page = browser.new_page() # Criar uma nova página
    
    page.goto("https://playwright.dev/python") # Navegar através do link
    
    docs_button = page.get_by_role('link', name="Docs") # Jeito de pegar um determinado elemento utilizando o role
    docs_button.click() # Gera a ação click 
    
    print("Docs url: ", page.url) # Link resultante após o direcionamento do botão: https://playwright.dev/python/docs/intro
    
    browser.close()