from django.db import models
import geocoder


class Location(models.Model):
    location_id  = models.AutoField(primary_key = True)
    location_name = models.CharField(max_length = 256)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    def __str__(self):
        return self.location_name
        
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.location_name).lat
        self.longitude = geocoder.osm(self.location_name).lng
        return super().save(*args, **kwargs)


class Crime(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_crime = models.CharField(max_length=255)
    description_of_crime = models.CharField(max_length = 255)
    date_of_crime = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.type_of_crime} at {self.location}'




class Crime(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_crime = models.CharField(max_length=255)
    description_of_crime = models.CharField(max_length=255)
    date_of_crime = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.type_of_crime} at {self.location}'