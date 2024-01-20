import os
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heatmapAPI.settings")
django.setup()
from core.models import Location  # Replace 'myapp' with the name of your Django app

data = [
    (20,"Calawagan (Kalawagan)", 15.533110, 121.034930),
    (25,"City Supermarket/Bayan (Poblacion)", 15.4882, 120.9636),
    (26,"Communal", 15.5336, 121.0421),
    (30,"Dicarma (Poblacion)", 15.4844, 120.9706),
    (43,"Lourdes(Matungal-tungal)", 15.4964, 121.0134),
    (54,"Melojavilla (Poblacion)", 15.486, 120.9608),
    (55,"Nabao (Poblacion)", 15.4902, 120.9652),
    (67,"Rizdelis (Poblacion)", 15.4885, 120.9604),
    (75,"Sanbermicristi (Poblacion)", 15.48, 120.96),
    (83,"Sumacab South", 15.4479, 120.9561),
    (88,"Villa Ofelia Subdivision (Villa Ofelia-Caridad)", 15.4814, 120.9711),
    (89,"Zuleta District (Poblacion)", 15.4801, 120.9578),
]

for location_id, location_name, latitude, longitude in data:
    Location.objects.create(location_id=location_id, location_name=location_name, latitude=latitude, longitude=longitude)

# 26,Communal,15.5336,121.0421
# 30,Dicarma (Poblacion),15.4844,120.9706
# 43,Lourdes(Matungal-tungal),15.4964,121.0134
# 54,Melojavilla (Poblacion),15.486,120.9608
# 55,Nabao (Poblacion),15.4902,120.9652
# 67,Rizdelis (Poblacion),15.4885,120.9604
# 75,Sanbermicristi (Poblacion),15.48,120.96
# 83,Sumacab South,15.4479,120.9561
# 88,Villa Ofelia Subdivision (Villa Ofelia-Caridad),15.4814,120.9711
# 89,Zuleta District (Poblacion),15.4801,120.9578
