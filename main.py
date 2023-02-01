import math
import sys
import requests
from we import start


def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_to_find = " ".join(sys.argv[1:])
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
address_ll = ','.join(toponym_coodrinates.split())
search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}
response = requests.get(search_api_server, params=search_params)
json_response = response.json()
o = [','.join(toponym_coodrinates.split())]
if len(json_response["features"]) > 10:
    n = 10
else:
    n = len(json_response["features"])
for i in range(n):
    organization = json_response["features"][i]
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    point = organization["geometry"]["coordinates"]
    try:
        if organization["properties"]["CompanyMetaData"]['Hours']['Availabilities'][0]['TwentyFourHours']:
            time = 2
    except:
        time = 3
    if time == 3:
        try:
            a = organization["properties"]["CompanyMetaData"]['Hours']
            time = 1
        except:
            time = 3
    if time == 3:
        r = 'pmgrs'
    elif time == 2:
        r = 'pmgns'
    else:
        r = 'pmbls'
    org_point = "{0},{1}".format(point[0], point[1]) + f',{r}'
    o.append(org_point)
map_params = {
    "l": "map",
    'pt': '~'.join(o)
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
start(response)