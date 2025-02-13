#Essa classe é onde temos a parte lógica das aplicações dentro da nossa automatização. Aqui temos coisas como clickar em um botão, enviar um texto ou copiar um texto de determinado elemento.

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        
        self.web_element = None
        self.find()
        
    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        element.click()
        
        return None

    def text(self):
        txt = self.web_element.text
        
        return txt