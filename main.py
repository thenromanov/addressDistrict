import sys
import requests
from addressCoords import getAddressCoords

try:
    coords = getAddressCoords(' '.join(sys.argv[1:]))[0]
    geocoderServer = 'http://geocode-maps.yandex.ru/1.x/'
    geocoderParams = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode':  ','.join(map(str, coords)),
        'kind': 'district',
        'format': 'json'}
    jsonResponse = requests.get(geocoderServer, params=geocoderParams).json()
    print(jsonResponse['response']['GeoObjectCollection']
          ['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']
          ['Components'][-1]['name'])
except Exception as e:
    print(e)
