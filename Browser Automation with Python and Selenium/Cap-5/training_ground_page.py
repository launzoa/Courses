
#Essa é uma classe quqe diz respeito a ações dentro de determinada página, ficando fácil encontrar a passagem de elementos para nossa base_element para manipular depois.

from selenium.webdriver.common.by import By

from base_page import BasePage
from base_element import BaseElement
from locator import Locator
from selenium.webdriver.common.alert import Alert

class TrainingGroundPage(BasePage):
    
    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button1(self):
        locator = Locator(By.CSS_SELECTOR, "button#b1")
        
        return BaseElement(self.driver, locator)
    
    def alert(self):
        Alert(self.driver).accept()
    
        return None