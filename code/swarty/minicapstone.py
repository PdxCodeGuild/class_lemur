'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''

import requests
import pprint as ppr
import polyline as poly
import turtle as tle
#google api info
gmap_elev='https://maps.googleapis.com/maps/api/elevation/json?'
gmap_dir='https://maps.googleapis.com/maps/api/directions/json?'
key='AIzaSyDF_BWgak4g5AwJsPV6KU-QLtcfmqlGsaM'



#get polylines from gmap
origin='Portland, OR'
dest='Wilsonville, OR'

params_map={'key':key, 'origin':origin, 'destination':dest}

pull_map=requests.get(gmap_dir, params=params_map).json()

routelegs=pull_map['routes'][0]['legs'][0]['steps']

#Viewer for debug
ppr.pp(routelegs)
filename='capstone.csv'
with open(filename, 'w') as file:
    file.write(str(routelegs))

#Build lat/lon array using points from Gmap polyline





#Get elevation of each point and add to array
locations='39.7391536,-104.9847034|36.455556,-116.866667'
path='36.578581,-118.291994|36.23998,-116.83171'
samples=10
params_elev={'key':key, 'path':path, 'samples':samples}
pull_elev=requests.get(gmap_elev, params=params_elev).json()