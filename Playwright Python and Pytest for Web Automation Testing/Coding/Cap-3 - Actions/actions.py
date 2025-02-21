from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    
    page = browser.new_page()
    page.goto("https://bootswatch.com/default")
    
    
    page.locator("a#theme-menu").click() # Simples click
    page.get_by_role("button", name="Dark").locator("nth=0").click()
    page.get_by_role("link", name="Themes").dblclick() # Double click
    page.get_by_role('link', name="Features").locator("nth=0").hover() # Passar o mouse por cima do elemento.
    page.get_by_placeholder("Search").locator("nth=0").click(button="right") # Botão direito do mouse
    
    
    page.get_by_placeholder("Search").locator("nth=0").fill("Inserir texto") # Adicionar o texto em um elemento
    page.get_by_placeholder("Search").locator("nth=1").type("Outra forma de inserir texto") # Outra forma
     
    
    page.locator("input#optionsRadios2").check() # Marcar radios
    page.locator("input#flexCheckDefault").check() # Narcar checklist
    page.locator("input#flexCheckChecked").uncheck() # Desmarcar checklist
    
    
    page.locator("select#exampleSelect2").select_option("4") # Selecionar um valor de selection
 
    
    page.keyboard.press("Control+A") # Utilizar teclas do teclado
    
    
    file_input = page.locator("input#formFile")
    with page.expect_file_chooser() as file_info:
        file_input.click()
    
    file_chooser = file_info.value
    file_chooser.set_files("actions.py") # Exemplo completo de fazer um upload de determinado arquivo
    
    page.wait_for_timeout(3000)
    
    
    page.close()