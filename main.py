import os
import sys
from random import choice, randrange
import pygame
import requests


a = ['Азнакаево', 'Альметьевск', 'Арск', 'Бавлы', '	Болгар', 'Бугульма', 'Буинск',
     'Елабуга', 'Заинск', '	Зеленодольск', 'Иннополис', 'Казань',
     'Кукмор', 'Лаишево', 'Нижнекамск', 'Набережные Челны', 'Нурлат', 'Чистополь']
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}" \
                       f"&geocode={address}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
    else:
        raise RuntimeError(
            """Ошибка выполнения запроса:
                       {request}
                Http статус: {status} ({reason})""".format(
                request=geocoder_request, status=response.status_code, reason=response.reason))
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_ll_span(address):
    toponym = geocode(address)
    if not toponym:
        return (None, None)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ",".join([toponym_longitude, toponym_lattitude])
    envelope = toponym["boundedBy"]["Envelope"]
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0
    span = f"{dx},{dy}"
    return ll, span


def start(response, toponym_to_find):
    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    running = True
    n = 0
    pygame.mixer.music.load("233843.mp3")
    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                n = 1
                font = pygame.font.Font(None, 20)
                text = font.render(toponym_to_find, True, (randrange(255), randrange(255), randrange(255)))
        if n == 100:
            os.remove(map_file)
            toponym_to_find = choice(a)
            response = mama(toponym_to_find)
            if not response:
                print("Ошибка выполнения запроса:")
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            n = 0
        screen.blit(pygame.image.load(map_file), (0, 0))
        if n > 0:
            font = pygame.font.Font(None, 80)
            text = font.render(toponym_to_find, True, (randrange(255), randrange(255), randrange(255)))
            screen.blit(text, (0, 300))
            n += 1
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


def mama(toponym_to_find):
    map_params = {
        "ll": get_ll_span(toponym_to_find)[0],
        "spn": get_ll_span(toponym_to_find)[1],
        "l": "sat"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response


if __name__ == '__main__':
    toponym_to_find = choice(a)
    start(mama(toponym_to_find), toponym_to_find)
