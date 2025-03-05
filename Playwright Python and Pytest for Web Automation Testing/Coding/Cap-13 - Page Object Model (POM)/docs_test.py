from playwright.sync_api import Page, expect
from docs_class import Docs

def test_docs_url(page: Page):
    
    doc = Docs(page)
    
    doc.visit_docs()
    
    expect(doc.page).to_have_url("https://playwright.dev/python/docs/intro")

def test_search(page: Page):
    
    search = Docs(page)
    data = "Assertions"
    
    search.search(data)
    search.analytics()
    
    expect(search.inpt_search).to_have_value(data)
    

'''
Esse teste se consiste em trabalhar com classes externas e realizar o teste em páginas separadas
Nesse exemplo, estamos fazendo dois testes, um simples teste para comparar a url da página e 
outro teste para fazer uma busca e printar o resultado dessa busca no prompt. Aqui começa o básico
do nosso web scraping de fazer busca e selecionar para coletar os dados. Já fizemos isso em outras
aulas, porém aqui temos um sistema melhor construído com páginas que funcionam entre si
'''