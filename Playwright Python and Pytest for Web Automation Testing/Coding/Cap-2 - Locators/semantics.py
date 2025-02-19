from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    
    page.get_by_role('button', name="Primary").highlight()
    
    page.get_by_label("Email address").highlight()
    
    page.get_by_text("Basic Bootstrap").highlight()
    
    page.get_by_placeholder("Password").highlight()
    
    page.get_by_role("button", name="Primary").locator("nth=1").highlight()
    page.wait_for_timeout(3000)    
    

    page.goto("https://unsplash.com/pt-br")
    
    page.get_by_alt_text("Um carro dirigindo por uma rua coberta de neve").highlight()
    
    page.get_by_alt_text("Um carro dirigindo por uma rua coberta de neve").click()
    
    
    page.close()
    
# Esse foi um capítulo introdutório falando um pouco sobre os 'locators' semânticos, que são recomendados por serem mais estáveis e refletem a intenção do código.