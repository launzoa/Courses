from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as playwright:
        
        browser = await playwright.chromium.launch(headless=False, slow_mo=1000, channel="msedge")
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        
        print(await page.title())
        
        await browser.close()
        
asyncio.run(main())

'''
Nesse exemplo, temos uma programação de forma assíncrona, isso significa que as operações são feitas em paralelo. Nesse caso, há a necessidade de 
utilizar o await antes de uma determinada ação de navegação que supostamente dependeria de outra e seria executado de forma escalada em um programa síncrono.
'''