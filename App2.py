# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:23:24 2020
WebMap with Markers
@author: SowjanyaG
"""

import folium
map = folium.Map(location = [17.4,78.5],zoom_start = 12, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.CircleMarker([17.4,78.5],popup ="Hi I'm Marker", icon = folium.Icon(color='blue')))
fg.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(),
                            style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")