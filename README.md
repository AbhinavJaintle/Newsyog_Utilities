# Newsyog_Utilities
## Mumbai-Wards
```python
from chart_studio import plotly
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import pandas as pd
```


```python
init_notebook_mode(connected=True) 
```







```python
df = pd.read_csv("D:\Documents\mumbai_wards.csv")
geojsons="D:\Downloads\mumbai_wards.geojson",

```


```python
from urllib.request import urlopen
import json
import pandas as pd
```


```python
file = open("D:\Downloads\mumbai_wards.json",'r')

geo_json = json.load(file)

```


```python
df = pd.read_csv("D:\Documents\mumbai_wards.csv")
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ward</th>
      <th>slum_population</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0 Purushottamdas Thakurdas Road, Azad Maidan, ...</td>
      <td>28.88</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0 Kalyan Street, Dana Bandar, Mandvi, Mumbai</td>
      <td>13.33</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Silva Building, Jagannath Shankar Seth Road, K...</td>
      <td>0.00</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>vinod buildnig, Raghavji Road, Gowalia Tank, C...</td>
      <td>9.95</td>
      <td>D</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0 Sant Savata Mali Marg, Byculla West, Chinchp...</td>
      <td>11.86</td>
      <td>E</td>
    </tr>
  </tbody>
</table>
</div>




```python
from shapely.geometry import shape
```


```python
center_pos = {}
features = geo_json['features']
for feature in features:
    k = feature['properties']['DISPLAY_NAME']
    s = shape(feature["geometry"])
    p = s.centroid
    center_pos[k] = list(p.coords)
```


```python
import plotly.graph_objects as go
import plotly.express as px
```


```python
mapbox_access_token = "pk.eyJ1IjoiamFpbnRsZSIsImEiOiJjbDN0OG40czUxNTlyM2lsdG96dnNqbnRkIn0.pmtJw4aoMUFzEEhjNhanhA"
```


```python
fig = go.Figure()

# for k,v in center_pos.items():
#     #print(k,v)
#     val = df[df['ward'] == k]['slum_population']
    
#     try:
#         if float(format(val.values[0]))>26.0:
#                 colour='white'
#         else:
#                 colour='black'
#         val = format(val.values[0])+'%'       
#     except IndexError:
#         val = '{:1}'.format(1)
    
    
#     fig.add_trace(go.Scattermapbox(
#         lat=[center_pos[k][0][1]],
#         lon=[center_pos[k][0][0]],
#         mode='text',
#         textfont=dict(
#             color = colour,
#             size=12,
#         ),
#         text=val,
#         showlegend=False
# ))
```


```python
fig.add_trace(go.Choroplethmapbox(
    geojson=geo_json, 
    locations=df['name'],
    featureidkey="properties.DISPLAY_NAME",
    z=df['slum_population'],
    colorscale="Reds",
    marker_opacity=0.7,
    marker_line_width=0
))
fig.update_layout(
    mapbox_accesstoken=mapbox_access_token,
#     mapbox_style="carto-positron",
    mapbox_zoom=4,
    mapbox_center = {"lat": 22.5, "lon": 81.0}
)

fig.update_layout(autosize=False,
                  height=1200,
                  width=1600,
                  margin={"r":0,"t":0,"l":0,"b":0},
                 )
fig.show()
```





```python

```

