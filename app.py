import json

from aiohttp import web

from project.get_weather import get_weather

routes = web.RouteTableDef()


@routes.get('/weather/{cities}')
async def weather(request):
    cities = request.match_info['cities'].split(',')
    cities_data = {}
    for city in cities:
        response = await get_weather(city=city)
        cities_data[city] = response['list'][0]
    with open('city_weather.json', 'w') as file:
        json.dump(cities_data, file, ensure_ascii=False, indent=4)
    return web.Response(body=json.dumps(cities_data))

app = web.Application()
app.add_routes(routes)
web.run_app(app)
