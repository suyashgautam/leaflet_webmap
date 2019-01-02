# leaflet_webmap
Webmaps for data analysis using folium and python

This is a sample project i did to analyse world population and to analyse the Volcanoes region in USA

Purpose of Volcanoes_USA.txt

This file contains address and latitude and longitude about the location of volcanoes in USA

We could have used geopy to to get the latitude and longitude of the coordinates but to reduce the complexity i have did it earlier so the file contains latitude and longitude and by using these is the first part we are marking the location and they are differentiated by their elevation which can be seen through their color

Purpose of shape.zip

step 1- Extract this zip folder
step 2- This folder contains 6 files out of which only shp file is important since folium cannot read shp file so we need to convert it into json or geojson file to convert this shp file into json or geo json use the following site

                                      https://ogre.adc4gis.com/
* I have included the converted file "convert.json"

To Execute the code simply install folium by using the command

pip install folium

Install Pandas

pip install pandas

Execute the code by typing

python Webmap.py in the terminal

A file names test.html will be stored in the same directory 
Open this file using browser
