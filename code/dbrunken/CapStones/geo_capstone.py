from geopy.geocoders import Nominatim
import easygui
import requests
import pprint
from secrets import secret_key_address, secret_key_direct


geolocator = Nominatim(user_agent='locator')

locations = [
    {'key': secret_key_address},
    { #location 1
        'latlng': '',
        'street': '',
        'city': '',
        'county': '',
        'state': '',
        'country': '',
        'postal_code': '',
        'type': ''
    },
    { #location 2
        'latlng': '',
        'street': '',
        'city': '',
        'county': '',
        'state': '',
        'country': '',
        'postal_code': '',
        'type': ''
    }
]

# location1 = geolocator.geocode("611 SW Kingston Ave, Portland OR, 97025")
location1 = geolocator.geocode(easygui.enterbox(msg="Enter start address: "))

# location2 = geolocator.geocode("5000 N Willamette Blvd, Portland, OR 97203")
location2 = geolocator.geocode(easygui.enterbox(msg="Enter finish address: "))




easygui.msgbox(msg=(f'{location1.address}, {location2.address}'), title=' ', ok_button='OK')

response = requests.get(f'http://www.mapquestapi.com/geocoding/v1/address?key={secret_key_address}&location={location1.address}')
response = response.json()
location1_lat_lng = response['results'][0]['locations'][0]['latLng']

response = requests.get(f'http://www.mapquestapi.com/geocoding/v1/address?key={secret_key_address}&location={location2.address}')
response = response.json()
location2_lat_lng = response['results'][0]['locations'][0]['latLng']


params = {
    'key': secret_key_direct,
    'from': f'{location1.latitude},{location1.longitude}',
    'to': f'{location2.latitude}, {location2.longitude}',
    'leg': {
        'street': '',
        'direction': '',
        'manuever': '',
        'distance': '',
        'narrative': ''
    }
}
# print(params)
response = requests.get(f'http://open.mapquestapi.com/directions/v2/route', params=params)

response = response.json()
route = response.get('route')
legs = route.get('legs')


step = 1
for leg in legs:
    for maneuver in leg['maneuvers']:
        easygui.msgbox(msg=(f'{step}.  {maneuver["narrative"]}, for {maneuver["distance"]} miles.'))
        print(f'{step}.  {maneuver["narrative"]}, for {maneuver["distance"]} miles.')
        step += 1
