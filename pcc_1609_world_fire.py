# Chapter 16: Try It Yourself. 16-9: World Fire.

import pandas as pd
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
df_fire = pd.read_csv('MODIS_C6_1_Global_7d.csv')

hover_texts = df_fire[['brightness', 'confidence']]

# Plotting the extracted data.
data = [{
    'type': 'scattergeo',
    'lon': df_fire['longitude'],
    'lat': df_fire['latitude'],
    'text': hover_texts,
    'marker': {
        'color': df_fire['confidence'],
        'colorscale': 'Reds',
        'colorbar': {'title': 'confidence'},
    },
}]
my_layout = Layout(title='7-day World Active Fire')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_active_fire.html')
