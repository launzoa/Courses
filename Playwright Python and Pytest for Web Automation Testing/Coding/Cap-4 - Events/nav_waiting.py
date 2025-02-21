from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    page = browser.new_page()
    
    time_start = perf_counter()
    #page.goto("https://playwright.dev/python/", wait_until="load") O tempo esperado para a página abrir foi de:  1.34
    #page.goto("https://playwright.dev/python/", wait_until="commit") O tempo esperado para a página abrir foi de:  1.08
    #page.goto("https://playwright.dev/python/", wait_until="domcontentloaded") O tempo esperado para a página abrir foi de:  1.33
    #page.goto("https://playwright.dev/python/", wait_until="networkidle") O tempo esperado para a página abrir foi de:  1.99
    
    time_taken = perf_counter() - time_start
    print("O tempo esperado para a página abrir foi de: ", round(time_taken, 2))
    
    browser.close()
    
    '''
    Nesse arquivos temos as diferentes 'aberturas' de um navegador pelo parâmetro wait_until dentro da função goto()
    Temos o valor 'load', que tem um tempo médio de carregamento, ele abre praticamente todos os eventos dentro do navegador
    O valor 'commit' é o mais rápido, porque o seu carregamento se dá antes dos pacotes DOM.
    'domcontentloeaded' é similar ao 'load', porém costuma ser ligeiramente mais rápido porque não necessita de carregar todos os eventos, como as imagens por exemplo
    Como o nome sugere, 'networkidle', é o carregamento da página junto com as suas funções de rede, consequentemente, a mais demorada forma de carregamento.
    '''