'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''

import requests



gmap_elev='https://maps.googleapis.com/maps/api/elevation/json?'

api='AIzaSyDF_BWgak4g5AwJsPV6KU-QLtcfmqlGsaM'
locations='39.7391536,-104.9847034|36.455556,-116.866667'
path='36.578581,-118.291994|36.23998,-116.83171'
samples=10

params={'key':api, 'locations':locations}



pull=requests.get(gmap_elev, params=params)
print(pull.json())