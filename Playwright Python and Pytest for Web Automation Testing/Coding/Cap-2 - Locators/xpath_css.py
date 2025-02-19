from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    
    page.locator("//h1[@id='navbars']").highlight()
    
    page.locator("//p[@class='lead']/../h1").highlight()
    
    page.locator("a.navbar-brand").highlight()
    
    page.locator("h1#typography").highlight()
    page.wait_for_timeout(3000)
    
    page.close()
    
    
# Aqui são alguns outros 'locatores', CSS_Select e XPath. Não são muito recomendados, porém ainda podem ter seu uso, principalmente pensando em parentesco de elementos, o xpath funciona bem