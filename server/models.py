from django.db import models
from accounts.models import User

class SmartFarm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sfid = models.IntegerField()

# Create your models here.
class SmartFarmSensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # sfid = models.ForeignKey(SmartFarm, on_delete=models.CASCADE, db_column="sfid")
    remotepower = models.BooleanField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    light = models.IntegerField()
    soil = models.IntegerField()
    
    ledpower = models.BooleanField()
    ledstate = models.BooleanField()
    ledtoggle = models.BooleanField()
    ledautotoggle = models.BooleanField()
    ledstarttimevalue = models.IntegerField()
    ledstartminutevalue = models.IntegerField()
    ledendtimevalue = models.IntegerField()
    ledendminutevalue = models.IntegerField()
    
    waterpumppower = models.BooleanField()
    waterpumpstate = models.BooleanField()
    waterpumptoggle = models.BooleanField()
    waterpumpautotoggle = models.BooleanField()
    waterpumpstarttime = models.IntegerField()
    waterpumprunningtime = models.IntegerField()
    waterlevelvoltage = models.FloatField()
    watertemperature = models.FloatField()
    
    fanpower = models.BooleanField()
    fanstate = models.BooleanField()
    fantoggle = models.BooleanField()
    fanautotoggle = models.BooleanField()
    fanstarttimevalue = models.IntegerField()
    fanstartminutevalue = models.IntegerField()
    fanendtimevalue = models.IntegerField()
    fanendminutevalue = models.IntegerField()

    doorpower = models.BooleanField()
    doorstate = models.BooleanField()
    doortoggle = models.BooleanField()
    doorautotoggle = models.BooleanField()
    doorstarttimevalue = models.IntegerField()
    doorstartminutevalue = models.IntegerField()
    doorendtimevalue = models.IntegerField()
    doorendminutevalue = models.IntegerField()
    
    waterlevelwarning = models.TextField(auto_created=True, null=True)
    watertempwarning = models.TextField(auto_created=True, null=True)
    tempwarning = models.TextField(auto_created=True, null=True)
    humwarning = models.TextField(auto_created=True, null=True)
    soilwarning = models.TextField(auto_created=True, null=True)
