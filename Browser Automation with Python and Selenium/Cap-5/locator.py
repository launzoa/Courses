#Simples estrutura de dados de tupla para armazenar a localização do nosso elemento, com o by: ID, Name, Xpath, CSSelector... Além do valor, button#b1 por exemplo.

from collections import namedtuple

Locator = namedtuple('Locator', ['by', 'value'])