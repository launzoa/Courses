from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from locator import Locator

class TrialPage(BasePage):
    
    url = 'https://techstepacademy.com/trial-of-the-stones'
    
    @property
    def inpt1(self):
        locator = Locator(By.CSS_SELECTOR, "input#r1Input")
        
        return BaseElement(self.driver, locator)
    
    @property
    def btn1(self):
        locator = Locator(By.CSS_SELECTOR, "button#r1Btn")
        
        return BaseElement(self.driver, locator)
    
    @property
    def secret_word(self):
        locator = Locator(By.CSS_SELECTOR, "div#passwordBanner > h4")
        
        return BaseElement(self.driver, locator)

    @property
    def inpt2(self):
        locator = Locator(By.CSS_SELECTOR, "input#r2Input")
        
        return BaseElement(self.driver, locator)
    
    @property
    def btn2(self):
        locator = Locator(By.CSS_SELECTOR, "button#r2Butn")
        
        return BaseElement(self.driver, locator)