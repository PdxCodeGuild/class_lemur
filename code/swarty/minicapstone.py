'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''
import altair as alt 
from secrets import gmap_key
from altair.vegalite.v4.schema.channels import Latitude2
import requests
import pprint as ppr
from polyline import decode
from time import sleep
import turtle as tle
from haversine import haversine as haver
#google api info
gmap_elev='https://maps.googleapis.com/maps/api/elevation/json?'
gmap_dir='https://maps.googleapis.com/maps/api/directions/json?'
key=gmap_key






#get polylines from gmap
origin='29744 Town Center Loop W, Wilsonville, OR 97070'
dest='16482 SW Langer Dr, Sherwood, OR 97140'

params_map={'key':key, 'origin':origin, 'destination':dest}

pull_map=requests.get(gmap_dir, params=params_map).json()
#Build lat/lon and dist array using points from Gmap polyline

pline_coord=[]
routelegs=pull_map['routes'][0]['legs'][0]['steps']
for leg in routelegs:
    i=routelegs.index(leg)
    pline_enc=routelegs[i]['polyline']['points']
    points=decode(pline_enc)
    #removing points within 100m of each other
    i=0
    j=len(points)-1
    while i < j:
        if round(points[i][0],3) == round(points[i+1][0],3) and round(points[i][1],3) == round(points[i+1][1],3):
            points.pop(i+1)
        else:
            i+=1
        j=len(points)-1
    pline_coord.extend(points)
coords=['']
j=0
i=0
for coord in pline_coord:
    lat=coord[0]
    lon=coord[1]
    coords[j]+=f'{lat},{lon}|'
    i+=1
    if i>511: #max pull is 512 for elevation points
        i=0
        j+=1
        coords.append('')




#Get elevtion for each point.
elevs=[]
for i in range(len(coords)):
    coords[i]=coords[i].strip('|')
    params_elev={'key':key, 'locations':coords[i]}
    pull_elev=requests.get(gmap_elev, params=params_elev).json()
    elevs.extend(pull_elev['results'])
    if len(coords) != 0:
        sleep(1)
#cleanup data and get distance points instead of coordinates.
i=0
dist=0
for elev in range(len(elevs)):
    el_data=(str(elev['elevation'],dist)+'\n')
    coord_1=(elev['location']['lat'],elev['location']['lng'])
    coord_2=(elevs[i+1]['location']['lat'],elevs[i+1]['location']['lng'])
    leg_dist=haversine(coord_1,coord_2)
    dist+=leg_dist


# chart=alt.Chart(elevs).mark_area().encode(
#     x="year:T",
#     y="net_generation:Q",
#     color="source:N"
# )
# chart.save('chart.html')


#Viewer for debug
ppr.pp(elevs)
filename='secrets.csv'
with open(filename, 'w') as file:
    file.write(el_data)
