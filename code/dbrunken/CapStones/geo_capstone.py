from geopy.geocoders import Nominatim
import easygui
import requests
from secrets import secret_key


geolocator = Nominatim(user_agent='locator')

# location1 = geolocator.geocode(easygui.enterbox(msg="Enter start street address: "))
location1 = geolocator.geocode("611 SW Kingston Ave, Portland OR, 97025")


# location2 = geolocator.geocode(easygui.enterbox(msg="Enter finish street address: "))
location2 = geolocator.geocode("5000 N Willamette Blvd, Portland, OR 97203")

# print(location.address)


easygui.msgbox(msg=(f'{location1.address}, {location2.address}'), title=' ', ok_button='OK')
# easygui.msgbox(msg=(f'{location2.address}'), title=' ', ok_button='OK', image=None, root=None)

params = {
    'key': secret_key,
    'from': location1,
    'to': location2,
    'leg': {
        'street': '',
        'direction': '',
        'manuever': '',
        'distance': '',
        'narrative': ''
    }
}

response = requests.get(f'http://open.mapquestapi.com/directions/v2/route?key={secret_key}&from={location1}&to={location2}', params=params)

response = response.json()
route = response.get('route')
legs= route.get('legs')
# print(legs[0]['maneuvers'][0].keys())

step = 1
for leg in legs:
    for maneuver in leg['maneuvers']:
        print(f'{step}.  {maneuver["narrative"]}, for {maneuver["distance"]} miles.')
        # easygui.msgbox(msg=f'{step}.  {maneuver["narrative"]}, for {maneuver["distance"]} miles.', title=' ', ok_button='OK')
        step += 1
# print(route, route.keys())
# print(response.keys())
# easygui.msgbox(msg=(f'{response}'), title=' ', ok_button='OK')