from playwright.sync_api import sync_playwright


def on_download(download):

    download.save_as("noite.jpg")
    
    
with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

    page.once("download", on_download)
    
    btn = page.get_by_role('link', name="Baixar gratuitamente")

    with page.expect_download() as download_info:
        btn.click()    
        
    browser.quit()
    
# Simples programa de download de uma imagem, nele utilizamos o with e também utilizamos o o listening 'once' para chamar o evento que queremos (download) apenas uma vez