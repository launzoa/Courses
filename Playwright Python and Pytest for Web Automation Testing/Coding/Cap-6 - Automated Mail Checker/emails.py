from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
    
    context = browser.new_context(
        storage_state="Coding/Cap-5 - Authentication/storage_state.json"
    )
    
    page = context.new_page()
    page.goto("https://gmail.com")
    
    emails = page.locator("div.UI table tr")
    new_emails = []
    
    for email in emails.all():
        new_email = email.locator("td ul li[data-tooltip='Mark as read']").count() == 1
        
        if new_email:
        
            name_email = email.locator("td div span span").locator("nth=1").inner_html()
            title_email = email.locator("td div span span").locator("nth=2").inner_html()
        
            new_emails.append((name_email, title_email))
    
    if len(new_emails) == 0:
        print("No new email found :(")
        
    else:
        print("We found a new email :)")
        for mail in new_emails:
            print(f"Name: {mail[0]}, text: {mail[1]}")
            
    page.pause()

    context.close()
    
    page.close()
    

    '''
    A estrutura é básica do cookies_authenticator, capítulo 5. Porém, aqui temos uma verificação simples de novos emails.
    Com o cache da sessão, entramos diretamente logados dentro do gmail. A aba do gmail, é uma tabela padrão de linhas contendo em cada uma delas, um email.
    A parte mais díficil é conseguir diferenciar esse email de um já lido e um 'novo'. 
    Para diferenciar, foi necessário ir atrás do elemento 'mark as read', presente dentro do email que ainda não foi lido. 
    Foi feito um loop percorrendo todas as linhas dos emails presentes e comparando em cada iteração se essa linha estava presente o 'mark as read'. 
    Caso presente, esse email é considerado novo, portanto, novamente é feito uma busca por dois locators, um para o nome do email e outro para o breve título do mesmo e adicionado dentro de um array.
    Por fim, caso o tamanho do array seja 0, significa que não foi encontrado novos emails, caso contrário, os emails são mostrados no terminal com o nome e o breve título do mesmo.
    '''