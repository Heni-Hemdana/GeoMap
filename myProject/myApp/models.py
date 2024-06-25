from django.contrib.gis.db import models # ! gis 
#--------------Model Zone--------------------------

class Zone(models.Model):
    name_zone = models.CharField(max_length=100, primary_key=True)
    coords_polys = models.MultiPolygonField(null=True)

    def __str__(self):
        return f"{self.name_zone}"  
