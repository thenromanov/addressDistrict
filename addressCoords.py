import sys
import requests


def getAddressCoords(address):
    geocoderServer = 'http://geocode-maps.yandex.ru/1.x/'
    geocoderParams = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode':  address,
        'format': 'json'}
    jsonResponse = requests.get(geocoderServer, params=geocoderParams).json()
    toponym = jsonResponse['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    requestCoords = list(map(float, toponym['Point']['pos'].split()))
    toponymCorners = jsonResponse['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    lowerCorner = list(map(float, toponymCorners['lowerCorner'].split()))
    upperCorner = list(map(float, toponymCorners['upperCorner'].split()))
    return [requestCoords, lowerCorner, upperCorner]


def main():
    try:
        address = ' '.join(sys.argv[1:])
        print(*getAddressCoords(address))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
