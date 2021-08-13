import altair as alt 
from secrets import gmap_key
import requests
import pprint as ppr
from vega_datasets import data, local_data
from vega_datasets.core import Dataset





source = 'data.iowa-electricity()'
print(source)
chart=alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)
chart.save('chart.html')