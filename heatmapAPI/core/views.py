



import folium
from folium import plugins
from django.shortcuts import render
from .models import Crime  # Import your Crime model or adjust the import as needed

def index(request):
    # Get crime data and corresponding location from the database
    crimes = Crime.objects.select_related('location')

    # Create a Folium map centered at a specific location
    map1 = folium.Map(location=[15.48586000, 120.96648000], tiles='CartoDB Dark Matter', zoom_start=14)

    # Create a list to store latitudes and longitudes for the heatmap
    heat_data = []

    # Iterate through each crime and add its location to the heat_data list
    for crime in crimes:
        heat_data.append([crime.location.latitude, crime.location.longitude])

    # Add HeatMap layer to the map using the heat_data
    map1.add_child(plugins.HeatMap(heat_data))

    # Add Fullscreen plugin to the map
    plugins.Fullscreen().add_to(map1)

    # Convert the map to HTML
    map_html = map1._repr_html_()

    context = {
        'map1': map_html,
    }

    return render(request, 'dashboard/index.html', context)
