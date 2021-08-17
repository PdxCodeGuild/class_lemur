'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''
import webbrowser as web
import pandas as pd
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

#get polylines from gmap
origin=input('Enter a staring address or coordinates: ')
dest=input('Enter an ending address or coordinates: ')

params_map={'key':gmap_key, 'origin':origin, 'destination':dest}

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
        if round(points[i][0],2) == round(points[i+1][0],2) and round(points[i][1],2) == round(points[i+1][1],2):
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
    params_elev={'key':gmap_key, 'locations':coords[i]}
    pull_elev=requests.get(gmap_elev, params=params_elev).json()
    elevs.extend(pull_elev['results'])
    if len(coords) != 0:
        sleep(.1)  #Be kind to the request server
#cleanup data and get distance points instead of coordinates.

i=1
dist=0
uphill=0
downhill=0
el_data={
    'altitude':[],
    'dist':[],
    'change':[],
    'uphill':[],
    'downhill':[]
    }
#el_data='altitude,dist\n' m to ft conversion is 3.28084
for elev in elevs:
    change=(elev['elevation']-elevs[0]['elevation'])
    el_data['altitude'].append(elev["elevation"]*3.28084)
    el_data['dist'].append(dist)
    el_data['change'].append(change*3.28084)
    el_data['uphill'].append(uphill*3.28084)
    el_data['downhill'].append(downhill*3.28084)
    if i==(len(elevs)):
        break
    coord_1=(elev['location']['lat'],elev['location']['lng'])
    coord_2=(elevs[i]['location']['lat'],elevs[i]['location']['lng'])
    leg_dist=haver(coord_1,coord_2, unit='mi') #calc approx distance between geo points using Haversine coordinate translation
    dist+=leg_dist
    change_leg=elevs[i]['elevation']-elev['elevation']
    if change_leg > 0:
        uphill+=change_leg
    else:
        downhill+=change_leg
    i+=1
chart_data=pd.DataFrame(el_data)

chart_data.to_csv('data.csv')
# with open(filename, 'w') as file:
#     file.write(chart_data)
#brush = alt.selection(type='interval', encodings=['x'])
# Chart you can chose form
selection=alt.selection_multi(fields=['measurement'], bind='legend')

chart1=alt.Chart(chart_data).transform_fold(
    ['altitude',
     'change',
     'uphill',
     'downhill'],
    as_ = ['measurement', 'value']).mark_line(interpolate='basis').encode(
    alt.X('dist:Q', title='Miles Travelled'),
    alt.Y('value:Q', title='Height (ft)'),
    alt.Color('measurement:N')
)
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['dist'], empty='none')

selectors = alt.Chart(chart_data).mark_point().encode(
    x='dist:Q',
    opacity=alt.value(0),
).add_selection(nearest)

points = chart1.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
mynumber=float
text = chart1.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'value:Q' , alt.value(''), format=',.0f')
)
rules = alt.Chart(chart_data).mark_rule(color='gray').encode(
    x='dist:Q',
).transform_filter(
    nearest
)
chart=alt.layer(
    chart1, selectors, points, rules, text
).properties(
    width=1200, height=800
)

chart.save('chart.html')
web.open('file://C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/chart.html')