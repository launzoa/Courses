'''
# Importar a função sync_playwright
from playwright.sync_api import sync_playwright

# Iniciar o Playwright
playwright = sync_playwright().start()

# Abrir o navegador, utilizei o Edge
browser = playwright.chromium.launch(headless=False, slow_mo=500, channel="msedge")

# Criar uma nova página
page = browser.new_page()

# Navegar para o email
playwi
# Fechar o navegador
browser.close()

# Encerrar o Playwright
playwright.stop()
'''

# Esse é apenas um rascunho para o (REPL - Read-Eval-Print Loop)