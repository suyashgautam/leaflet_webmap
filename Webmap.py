
# coding: utf-8

# In[258]:


import pandas
import folium


# In[259]:


cord=pandas.read_csv("Volcanoes_USA.txt")
map=folium.Map([cord['LAT'].mean(),cord['LON'].mean()],zoom_start=2,tiles="Mapbox bright")

def color(ele):
    mini=int(min(cord['ELEV']))
    step=int(((max(cord['ELEV'])-min(cord['ELEV']))/3))
    if ele in range(mini,mini+step):
        col= 'orange'
    elif ele in range(mini+step,mini+step+step):
        col= 'red'
    else:
        col= 'black'
    return col

fg=folium.FeatureGroup(name="Volcano Locations")


# In[260]:


for lat,lon,name,elev in zip(cord['LAT'],cord['LON'],cord['NAME'],cord['ELEV']):
    fg.add_child(folium.Marker([lat,lon],popup=name,icon=folium.Icon(color=color(elev))))

map.add_child(fg)


# In[261]:


map.add_child(folium.GeoJson("convert.json",name='World-Population',style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'black'}))

map.add_child(folium.LayerControl())

map.save('test.html')

