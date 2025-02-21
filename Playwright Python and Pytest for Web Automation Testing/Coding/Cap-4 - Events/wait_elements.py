from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel='msedge')
    page = browser.new_page()
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

    link = page.get_by_role('link', name="2015")
    link.click()
    
    time_start = perf_counter()
    
    content = page.locator("div.col-md-12").first
    content.wait_for()
    
    time_taken = perf_counter() - time_start
    print("Tempo estimado para a abertura do conteúdo: ", round(time_taken, 2))
    
    page.close()
          
# Bascimanete um simples teste para abrir um elemento que libera outro elemento e fazermos uma captura de quanto tempo levou para abrir esse elemente e aparacer o seu conteúdo