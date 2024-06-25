from django.shortcuts import render
from .models import Zone 
from django.contrib.gis.geos import GEOSGeometry

# le nom de view qui va recuperer 
def index(request): 
    if request.method == 'POST':
        #recupération
        name_zone=request.POST.get('name_zone')
        Multi_polygone= request.POST.get('coords_polys')

        print(Multi_polygone)
        #conversion 
        Instance_Multi_polygone = GEOSGeometry(Multi_polygone, srid=4326) 

        #enregistrement
        données_zone=Zone(name_zone=name_zone, coords_polys=Instance_Multi_polygone)
        données_zone.save() 

    return render(request,'myApp/index.html')



