import aiohttp
import asyncio

from project.settings import URL


async def get_weather(city: str):
    headers = {'Content-Type': 'application/json'}
    async with aiohttp.ClientSession(headers=headers) as session:
        url = URL.format(city)
        async with session.get(url, verify_ssl=False) as resp:
            response = await resp.json()
    return response
