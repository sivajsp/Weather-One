from django.db import models

class weather_class(models.Model):
        forecast_icon = models.CharField(max_length = 20)
        description = models.CharField(max_length =20)
        date = models.DateTimeField()
        location = models.CharField(max_length=20)
        degree = models.SmallIntegerField()
        cloud_percentage = models.SmallIntegerField()
        windspeed = models.SmallIntegerField()
        wind_direction = models.CharField(max_length = 20)


# Create your models here.
