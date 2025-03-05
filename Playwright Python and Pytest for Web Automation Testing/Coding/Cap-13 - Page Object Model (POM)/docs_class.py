from playwright.sync_api import Page

class Docs:
    
    def __init__(self, page: Page):
            
        self.page = page
        self.page.goto("https://playwright.dev/python")
            
        self.btn_doc = self.page.get_by_role("link", name="Docs")
        self.inpt_search = self.page.locator("input.DocSearch-Input")
        self.div_result_search = self.page.locator("span.DocSearch-Hit-title")
        
    def visit_docs(self):
        
        self.btn_doc.click()
    
    def open_search(self):
        
        self.page.keyboard.press("Control+KeyK")
        
    def search(self, query):
        
        self.open_search()
        self.inpt_search.fill(query)
        
    def analytics(self):
        
        for result in self.div_result_search.all():
            print(result.inner_text())
        
'''
Classe para o nosso teste docs_test
Essa classe tem funcionalidades simples que realizar os nossos testes
'''