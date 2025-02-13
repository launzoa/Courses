#Essa é uma classe base da página, onde é encontrado as informações sobre o tipo do driver da página e a url da mesma. Exemplo -> Edge() e 'http://www.google'. Serve de base para outras classes

class BasePage(object):
    
    url = None
    
    def __init__(self, driver):
        self.driver = driver
        
    def go(self):
        self.driver.get(self.url)