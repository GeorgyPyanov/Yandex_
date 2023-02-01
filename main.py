import sys
import requests
from we import get_ll_span, start


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
map_params = {
    "ll": get_ll_span(toponym_to_find)[0],
    "spn": get_ll_span(toponym_to_find)[1],
    "l": "map",
    'pt': ','.join(toponym_coodrinates.split())
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
start(response)