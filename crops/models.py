from django.db import models

# Create your models here.
class SmartFarmCrop(models.Model):
    name = models.CharField(max_length=20)
    day = models.IntegerField()
    ndvi = models.IntegerField(null=True)