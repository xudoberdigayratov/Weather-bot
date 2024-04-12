import asyncio

import requests
from bs4 import BeautifulSoup as BS
import aiohttp

# def pogoda(city):
#     try:
#         url = "https://sinoptik.ua/{}".format(city)
#         response = requests.get(url).content
#         html = BS(response, "html.parser")
#         result = {}
#         for x in html.select('#content'):
#             min = x.select('.temperature .min')[0].text
#             max = x.select('.temperature .max')[0].text
#             result['min'] = min[5:]
#             result['max'] = max[6:]
#         return result
#     except Exception as e:
#         print(e)
#         return False


async def pogoda(city):
    try:
        url = "https://sinoptik.ua/{}".format(city)
        result = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = BS(await response.text(), "html.parser")
                for x in html.select('#content'):
                    min = x.select('.temperature .min')[0].text
                    max = x.select('.temperature .max')[0].text
                    result['min'] = min[5:]
                    result['max'] = max[6:]

        return result
    except Exception as e:
        print(e)
        return False
