'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''
 
from secrets import secret_key
import requests
import pprint as ppr
from polyline import decode
from time import sleep
import turtle as tle
#google api info
gmap_elev='https://maps.googleapis.com/maps/api/elevation/json?'
gmap_dir='https://maps.googleapis.com/maps/api/directions/json?'
key=secret_key



#get polylines from gmap
origin='Portland, OR'
dest='Wilsonville, OR'

params_map={'key':key, 'origin':origin, 'destination':dest}

pull_map=requests.get(gmap_dir, params=params_map).json()
#Build lat/lon and dist array using points from Gmap polyline

pline_coord=[]
routelegs=pull_map['routes'][0]['legs'][0]['steps']
for leg in routelegs:
    i=routelegs.index(leg)
    pline_enc=routelegs[i]['polyline']['points']
    pline_coord.extend(decode(pline_enc))
coords=['']
j=0
i=0
for coord in pline_coord:
    lat=coord[0]
    lon=coord[1]
    coords[j]+=f'{lat},{lon}|'
    i+=1
    if i>511:
        i=0
        j+=1
        coords.append('')
elev=[]
for i in range(len(coords)):
    coords[i]=coords[i].strip('|')
#Get elevation of each point and add to array - Max points per pull is 512
#locations='39.7391536,-104.9847034|36.455556,-116.866667'
#path='36.578581,-118.291994|36.23998,-116.83171'
#samples=10
    params_elev={'key':key, 'locations':coords[i]}
    pull_elev=requests.get(gmap_elev, params=params_elev).json()
    elev.extend(pull_elev['results'])
    sleep(1)


#Viewer for debug
ppr.pp(elev)
filename='capstone.csv'
with open(filename, 'w') as file:
    file.write(str(elev))