from rest_framework.serializers import ModelSerializer

from .models import SmartFarmCrop

class SmartFarmCropModelSerializer(ModelSerializer):
    class Meta:
        model = SmartFarmCrop
        fields = '__all__'