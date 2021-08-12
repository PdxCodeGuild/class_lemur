from geopy.geocoders import Nominatim
import easygui
import requests
from .secrets import secret_key


geolocator = Nominatim(user_agent='locator')

location1 = geolocator.geocode(easygui.enterbox(msg="611 SW Kingston Ave "))
location2 = geolocator.geocode(easygui.enterbox(msg="777 NE Martin Luther King Jr Blvd "))
#611 SW Kingston Ave returns Portland Japanese Garden... etc
# print(location.address)


easygui.msgbox(msg=(f'{location1.address},\n {location2.address}'), title=' ', ok_button='OK', image=None, root=None)
# easygui.msgbox(msg=(f'{location2.address}'), title=' ', ok_button='OK', image=None, root=None)

params = {
    'key': secret_key,
    'from': location1,
    'to': location2,
    'leg': {
        'street': '',
        'direction': '',
        'manuever': '',
    }
}

response = requests.get('http://open.mapquestapi.com/directions/v2/route', params=params)

response = response.json()
print(response)