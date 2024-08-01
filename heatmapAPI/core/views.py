
import folium
from folium import plugins
from django.shortcuts import render
from .models import Crime  # Import your Crime model or adjust the import as needed
from folium.plugins import MarkerCluster

def index(request):
    # Get crime data and corresponding location from the database
    crimes = Crime.objects.select_related('location')

    # Create a Folium map centered at a default location
    map1 = folium.Map(location=[15.48586000, 120.96648000], tiles='CartoDB Dark Matter', zoom_start=14)

    # Create a MarkerCluster object
    marker_cluster = MarkerCluster().add_to(map1)

    # Iterate through each crime and add a marker to the cluster
    for crime in crimes:
        folium.Marker(
            location=[crime.location.latitude, crime.location.longitude],
            popup=f'Crime: {crime.type}, Date: {crime.date}'
        ).add_to(marker_cluster)

    # Add the HeatMap to the map
    map1.add_child(plugins.HeatMap(heat_data, radius=10, blur=15))
    
    # Add fullscreen button
    plugins.Fullscreen().add_to(map1)

    # Convert the map to HTML
    map_html = map1._repr_html_()

    context = {
        'map1': map_html,
    }

    return render(request, 'dashboard/index.html', context)

# meeded tp add PWA support of service-worker.js plus offline maps for map1