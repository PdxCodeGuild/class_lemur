'''

A Elevation API request takes the following form:


https://maps.googleapis.com/maps/api/elevation/outputFormat?parameters

where outputFormat may be either of the following values:

json (recommended), indicates output in JavaScript Object Notation (JSON); or
xml, indicates output in XML, wrapped within a <ElevationResponse> node.

'''

import requests



gmap_elev='https://maps.googleapis.com/maps/api/elevation/json?

api=AIzaSyDF_BWgak4g5AwJsPV6KU-QLtcfmqlGsaM

pull=requests.get(gmap_elev, params)