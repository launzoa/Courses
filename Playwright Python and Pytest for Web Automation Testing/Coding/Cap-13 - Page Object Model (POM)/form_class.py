from playwright.sync_api import Page

class Form:
    
    def __init__(self, page: Page):
        
        self.page = page
        self.page.goto("http://uitestingplayground.com/sampleapp")
            
        self.txt_user = page.get_by_role("textbox", name="User Name")
        self.txt_password = page.get_by_role("textbox", name="********")
        self.submit = page.get_by_role("button", name="Log In")
        
        self.resul = page.locator("label#loginstatus")


    def login(self, username, password):
        
        self.txt_user.fill(username)
        self.txt_password.fill(password)
        
        self.submit.click()
        
'''
Classe para o nosso teste de login
'''