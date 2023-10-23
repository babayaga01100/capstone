from rest_framework.serializers import ModelSerializer

from .models import SmartFarmSensor

class SmartFarmBaseModelSerializer(ModelSerializer):
    class Meta:
        model = SmartFarmSensor
        fields = '__all__'
        # exclude = ("")
    
class InfoListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = [ 
                #   'sfid', 
                  'remotepower', 
                  'temperature', 
                  'humidity']
        
class LedListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = ['ledpower', 
                  'ledstate', 
                  'ledtoggle', 
                  'ledautotoggle', 
                  'ledstarttimevalue', 
                  'ledstartminutevalue', 
                  'ledendtimevalue', 
                  'ledendminutevalue']
        
class WaterListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        filed = ['waterpumppower',
                'waterpumpstate',
                'waterpumptoggle',
                'waterpumpautotoggle',
                'waterpumpstarttime',
                'waterpumprunningtime',
                'waterlevelvoltage',
                'watertemperature']
class FanListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
            'fanpower',
            'fanstate',
            'fantoggle',
            'fanautotoggle',
            'fanstarttimevalue',
            'fanstartminutevalue',
            'fanendtimevalue',
            'fanendminutevalue'
        ]
        
class DoorListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
                'doorpower',
                'doorstate',
                'doortoggle',
                'doorautotoggle',
                'doorstarttimevalue',
                'doorstartminutevalue',
                'doorendtimevalue',
                'doorendminutevalue'
        ]
        
class WarningListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        field = [
                'waterlevelwarning',
                'watertempwarning',
                'tempwarning',
                'humwarning',
                'soilwarning'
        ]