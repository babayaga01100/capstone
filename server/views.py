import json
from requests import request
from rest_framework import authentication, permissions
from rest_framework import generics
from rest_framework import status

from django.db.models import Max
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

from django.shortcuts import render

from rest_framework.authtoken.models import Token

# from ..fcm_notification import send_push_notification, send_push_notification2, send_push_notification3, send_push_notification4, send_push_notification5

from .models import SmartFarmSensor, SmartFarm, User
from .serializers import DoorListModelSerializer, FanListModelSerializer, InfoListModelSerializer, LedListModelSerializer, SFSerializer, SmartFarmBaseModelSerializer, WarningListModelSerializer, WaterListModelSerializer

# 스마트팜 고유번호 확인
@api_view(['POST'])
@permission_classes([AllowAny])
def check_smartfarm_id_view(request):
    try:
        sfid = request.data['sfid']
        SmartFarm.objects.get(sfid=sfid)
        
        return Response({'message': '이미 등록되어 있는 스마트팜입니다.'}, status=400)
    except:
        return Response(status=200)    


# 스마트팜 등록      
@api_view(['POST'])
def register_smartfarm_view(request):
    # 사용자 가져오기
    try:
        user = User.objects.get(username=request.user)
    except:
        return Response({'message': '등록되어 있지 않은 사용자입니다.'}, status=404)
    
    # 스마트팜 등록하기
    sfid = request.data['sfid']
    smartfarm = SmartFarm.objects.create(user=user, sfid=sfid)
    smartfarm.save()
    
    return Response(status=200)


# 스마트팜 수정
@api_view(['POST'])
def modify_smartfarm_view(request):
    # 사용자 가져오기
    try:
        user = User.objects.get(username=request.user)
    except:
        return Response({'message': '등록되어 있지 않은 사용자입니다.'}, status=404)
    
    # 스마트팜 가져오기
    try:
        smartfarm = SmartFarm.objects.get(user=user)
        
        sfid = request.data['sfid']
        smartfarm.sfid = sfid
        smartfarm.save()
    except:
        return Response({'message': '등록되어 있는 스마트팜이 없습니다.'}, status=400)
    
    # 스마트팜 등록하기
    sfid = request.data['sfid']
    smartfarm = SmartFarm.objects.create(user=user, sfid=sfid)
    smartfarm.save()


# 스마트팜 삭제    
@api_view(['DELETE'])
def remove_smartfarm_view(request):
    try:
        sfid = request.data['sfid']
        smartfarm = SmartFarm.objects.get(sfid=sfid)
        smartfarm.delete()
        
        return Response(status=200)
    except:
        return Response({'message': '등록되어 있지 않은 스마트팜입니다.'}, status=404)
    

# class RegistrationSF(APIView):

#     def post(self, request):
#         # 사용자 가져오기
#         try:
#             user = User.objects.get(username=request.user)
#         except User.DoesNotExist:
#             return Response({'message': '등록되어 있지 않은 사용자입니다.'}, status=404)
        
#         # 스마트팜 등록하기
#         # 토큰 검증
#         # token = request.data.get('token')
#         # try:
#         #     user = User.objects.get(username=request.user)
#             # token_obj = Token.objects.get(key=token)
#             # user = token_obj.user  # 토큰에서 사용자 추출
#         # except Token.DoesNotExist:
#         #     return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

#         # 토큰이 유효하고 사용자가 인증되면 나머지 작업 수행
#         serializer = SFSerializer(data=request.data)
#         # print(serializer.data)
#         if serializer.is_valid():
#             user = User.objects.get(username=request.user)
#             # SmartFarm 모델의 user 필드에 사용자 연결
#             serializer.validated_data['username'] = user
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
class RaspberryView(APIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = SmartFarmBaseModelSerializer
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = list(SmartFarmSensor.objects.filter(id=latest_id).values()& SmartFarmSensor.objects.filter(user=request.user).values())
            # queryset = SmartFarmSensor.objects.filter(user=request.user)
            # queryset = list(SmartFarmSensor.objects.filter(id=latest_id).values())
            # smartfarm = list(SmartFarmSensor.objects.filter(user=request.user).values())
            return Response(queryset, status=status.HTTP_200_OK)

        except SmartFarmSensor.DoesNotExist:
            return Response({'message': '등록한 스마트팜이 없습니다.'}, status=404)
        

    def post(self, request):
        user = request.user
        # sfid = request.data['sfid']
        remotepower = request.data['remotepower']
        temperature = request.data['temperature']
        humidity = request.data['humidity']
        light = request.data['light']
        soil = request.data['soil']
        
        ledpower = request.data['ledpower']
        ledstate = request.data['ledstate']
        ledtoggle = request.data['ledtoggle']
        ledautotoggle = request.data['ledautotoggle']
        ledstarttimevalue = request.data['ledstarttimevalue']
        ledstartminutevalue = request.data['ledstartminutevalue']
        ledendtimevalue = request.data['ledendtimevalue']
        ledendminutevalue = request.data['ledendminutevalue']
    
        waterpumppower = request.data['waterpumppower']
        waterpumpstate = request.data['waterpumpstate']
        waterpumptoggle = request.data['waterpumptoggle']
        waterpumpautotoggle = request.data['waterpumpautotoggle']
        waterpumpstarttime = request.data['waterpumpstarttime']
        waterpumprunningtime = request.data['waterpumprunningtime']
        waterlevelvoltage = request.data['waterlevelvoltage']
        watertemperature = request.data['watertemperature']
    
        fanpower = request.data['fanpower']
        fanstate = request.data['fanstate']
        fantoggle = request.data['fantoggle']
        fanautotoggle = request.data['fanautotoggle']
        fanstarttimevalue = request.data['fanstarttimevalue']
        fanstartminutevalue = request.data['fanstartminutevalue']
        fanendtimevalue = request.data['fanendtimevalue']
        fanendminutevalue = request.data['fanendminutevalue']

        doorpower = request.data['doorpower']
        doorstate = request.data['doorstate']
        doortoggle = request.data['doortoggle']
        doorautotoggle = request.data['doorautotoggle']
        doorstarttimevalue = request.data['doorstarttimevalue']
        doorstartminutevalue = request.data['doorstartminutevalue']
        doorendtimevalue = request.data['doorendtimevalue']
        doorendminutevalue = request.data['doorendminutevalue']
    
        waterlevelwarning = request.data['waterlevelwarning']
        watertempwarning = request.data['watertempwarning']
        tempwarning = request.data['tempwarning']
        humwarning = request.data['humwarning']
        soilwarning = request.data['soilwarning']
        
        try:
            smartfarm = SmartFarmSensor.objects.filter(user_id=request.user)
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': '등록한 스마트팜이 없습니다.'}, status=404)
        
        
        SmartFarmSensor(
            user = user,
            # sfid = sfid,
            remotepower = remotepower,
            temperature = temperature,
            humidity = humidity,
            light = light,
            soil = soil,
            ledpower = ledpower,
            ledstate = ledstate,
            ledtoggle = ledtoggle,
            ledautotoggle = ledautotoggle,
            ledstarttimevalue = ledstarttimevalue,
            ledstartminutevalue = ledstartminutevalue,
            ledendtimevalue = ledendtimevalue,
            ledendminutevalue = ledendminutevalue,
            waterpumppower = waterpumppower,
            waterpumpstate = waterpumpstate,
            waterpumptoggle = waterpumptoggle,
            waterpumpautotoggle = waterpumpautotoggle,
            waterpumpstarttime = waterpumpstarttime,
            waterpumprunningtime = waterpumprunningtime,
            waterlevelvoltage = waterlevelvoltage,
            watertemperature = watertemperature,
            fanpower = fanpower,
            fanstate = fanstate,
            fantoggle = fantoggle,
            fanautotoggle = fanautotoggle,
            fanstarttimevalue = fanstarttimevalue,
            fanstartminutevalue = fanstartminutevalue,
            fanendtimevalue = fanendtimevalue,
            fanendminutevalue = fanendminutevalue,
            doorpower = doorpower,
            doorstate = doorstate,
            doortoggle = doortoggle,
            doorautotoggle = doorautotoggle,
            doorstarttimevalue = doorstarttimevalue,
            doorstartminutevalue = doorstartminutevalue,
            doorendtimevalue = doorendtimevalue,
            doorendminutevalue = doorendminutevalue,
            waterlevelwarning = waterlevelwarning,
            watertempwarning = watertempwarning,
            tempwarning = tempwarning,
            humwarning = humwarning,
            soilwarning = soilwarning,
        ).save()
        
        
        # if waterlevelwarning != '':
        #     send_push_notification()
        # elif watertempwarning != '':
        #     send_push_notification2()
        # elif tempwarning != '':
        #     send_push_notification3()
        # elif humwarning != '':
        #     send_push_notification4()
        # elif soilwarning != '':
        #     send_push_notification5()
        # else:
        #     Response({'No':'Message'})
            
        return Response({'su':'ccess_fcm'})

          
class InfoView(generics.ListAPIView):
# class InfoView(APIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = InfoListModelSerializer

    def post(self, request):
        remotepower = request.data['remotepower']
        
        latest_id = SmartFarmSensor.objects.latest('id').id
        SmartFarmSensor.objects.filter(id=latest_id).update(remotepower=remotepower)
        return Response({'su':'ccess_info'})

    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            
            # if not SmartFarmSensor.objects.filter(sfid=sfid).exists():
            #     return Response({'message': '해당 사용자 정보가 없습니다.'}, status=404)
            
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'Info Error.'}, status=404)

    #     if not SmartFarmSensor.objects.filter(
    #         # sfid=sfid,
    #         remotepower=remotepower,
    #         temperature=temperature,
    #         humidity=humidity
    #     ).exists():
    #         return Response({'message': 'Error'}, status=404)
    

    
class LedView(generics.ListAPIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = LedListModelSerializer
    
    def post(self, request):   
        ledtoggle = request.data['ledtoggle']
        ledautotoggle = request.data['ledautotoggle']
        ledstarttimevalue = request.data['ledstarttimevalue']
        ledstartminutevalue = request.data['ledstartminutevalue']
        ledendtimevalue = request.data['ledendtimevalue']
        ledendminutevalue = request.data['ledendminutevalue']

        latest_id = SmartFarmSensor.objects.latest('id').id
        SmartFarmSensor.objects.filter(id=latest_id).update(ledtoggle=ledtoggle, ledautotoggle=ledautotoggle, 
                                        ledstarttimevalue=ledstarttimevalue, ledstartminutevalue=ledstartminutevalue, 
                                        ledendtimevalue=ledendtimevalue, ledendminutevalue=ledendminutevalue)
        return Response({'su':'ccess_led'})
        
    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'LED Error.'}, status=404)
        
    
class WaterView(generics.ListAPIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = WaterListModelSerializer
    
    def post(self, request):   
        waterpumptoggle = request.data['waterpumptoggle']
        waterpumpautotoggle = request.data['waterpumpautotoggle']
        waterpumpstarttime = request.data['waterpumpstarttime']
        waterpumprunningtime = request.data['waterpumprunningtime']

        latest_id = SmartFarmSensor.objects.latest('id').id
        SmartFarmSensor.objects.filter(id=latest_id).update(waterpumptoggle=waterpumptoggle, waterpumpautotoggle=waterpumpautotoggle, 
                                        waterpumpstarttime=waterpumpstarttime, waterpumprunningtime=waterpumprunningtime)
        return Response({'su':'ccess_water'})
        
    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'Water Error.'}, status=404)
        
    
class FanView(generics.ListAPIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = FanListModelSerializer
    
    def post(self, request):   
        fantoggle = request.data['fantoggle']
        fanautotoggle = request.data['fanautotoggle']
        fanstarttimevalue = request.data['fanstarttimevalue']
        fanstartminutevalue = request.data['fanstartminutevalue']
        fanendtimevalue = request.data['fanendtimevalue']
        fanendminutevalue = request.data['fanendminutevalue']

        latest_id = SmartFarmSensor.objects.latest('id').id
        SmartFarmSensor.objects.filter(id=latest_id).update(fantoggle=fantoggle, fanautotoggle=fanautotoggle, 
                                        fanstarttimevalue=fanstarttimevalue, fanstartminutevalue=fanstartminutevalue, 
                                        fanendtimevalue=fanendtimevalue, fanendminutevalue=fanendminutevalue)
        return Response({'su':'ccess_fan'})
        
    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'Fan Error.'}, status=404)
    
class DoorView(generics.ListAPIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = DoorListModelSerializer
    
    def post(self, request):
        doortoggle = request.data['doortoggle']
        doorautotoggle = request.data['doorautotoggle']
        doorstarttimevalue = request.data['doorstarttimevalue']
        doorstartminutevalue = request.data['doorstartminutevalue']
        doorendtimevalue = request.data['doorendtimevalue']
        doorendminutevalue = request.data['doorendminutevalue']
        
        latest_id = SmartFarmSensor.objects.latest('id').id
        SmartFarmSensor.objects.filter(id=latest_id).update(doortoggle=doortoggle, doorautotoggle=doorautotoggle, 
                                        doorstarttimevalue=doorstarttimevalue, doorstartminutevalue=doorstartminutevalue, 
                                        doorendtimevalue=doorendtimevalue, doorendminutevalue=doorendminutevalue)
        return Response({'su':'ccess_door'})
        
    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'Door Error.'}, status=404)
    
class WarningView(generics.ListAPIView):
    # queryset = SmartFarmSensor.objects.all()
    serializer_class = WarningListModelSerializer
    
    def post(self, request):
        waterlevelwarning = request.data['waterlevelwarning']
        watertempwarning = request.data['watertempwarning']
        tempwarning = request.data['tempwarning']
        humwarning = request.data['humwarning']
        soilwarning = request.data['soilwarning']
        
        latest_id = SmartFarmSensor.objects.latest('id').id
        
        if waterlevelwarning != '':
            waterlevelwarning == ''
            SmartFarmSensor.objects.filter(id=latest_id).update(waterlevelwarning=waterlevelwarning)
        elif watertempwarning != '':
            watertempwarning == ''
            SmartFarmSensor.objects.filter(id=latest_id).update(watertempwarning=watertempwarning)
        elif tempwarning != '':
            tempwarning == ''
            SmartFarmSensor.objects.filter(id=latest_id).update(tempwarning=tempwarning)
        elif humwarning != '':
            humwarning == ''
            SmartFarmSensor.objects.filter(id=latest_id).update(humwarning=humwarning)
        elif soilwarning != '':
            soilwarning == ''
            SmartFarmSensor.objects.filter(id=latest_id).update(soilwarning=soilwarning)
        else:
            Response({'No':'Message'})
            
        return Response({'su':'ccess_warning'})
        
    def get_queryset(self):
        # 최신 ID 값을 기준으로 QuerySet 필터링
        try:
            latest_id = SmartFarmSensor.objects.latest('id').id
            queryset = SmartFarmSensor.objects.filter(id=latest_id)
            return queryset
        except SmartFarmSensor.DoesNotExist:
            return Response({'message': 'Warning Error.'}, status=404)
        
    
        # soil = request.get(soil=soil)
    
        # ledpower = request.get(ledpower=ledpower)
        # ledstate = request.get(ledstate=ledstate)
        # ledtoggle = request.get(ledtoggle=ledtoggle)
        # ledautotoggle = request.get(ledautotoggle=ledautotoggle)
        # ledstarttimevalue = request.get(ledstarttimevalue=ledstarttimevalue)
        # ledstartminutevalue = request.get(ledstartminutevalue=ledstartminutevalue)
        # ledendtimevalue = request.get(ledendtimevalue=ledendtimevalue)
        # ledendminutevalue = request.get(ledendminutevalue=ledendminutevalue)
    
        # waterpumppower = request.get(waterpumppower=waterpumppower)
        # waterpumpstate = request.get(waterpumpstate=waterpumpstate)
        # waterpumptoggle = request.get(waterpumptoggle=waterpumptoggle)
        # waterpumpautotoggle = request.get(waterpumpautotoggle=waterpumpautotoggle)
        # waterpumpstarttime = request.get(waterpumpstarttime=waterpumpstarttime)
        # waterpumprunningtime = request.get(waterpumprunningtime=waterpumprunningtime)
        # waterlevelvoltage = request.get(waterlevelvoltage=waterlevelvoltage)
        # watertemperature = request.get(watertemperature=watertemperature)
    
        # fanpower = request.get(fanpower=fanpower)
        # fanstate = request.get(fanstate=fanstate)
        # fantoggle = request.get(fantoggle=fantoggle)
        # fanautotoggle = request.get(fanautotoggle=fanautotoggle)
        # fanstarttimevalue = request.get(fanstarttimevalue=fanstarttimevalue)
        # fanstartminutevalue = request.get(fanstartminutevalue=fanstartminutevalue)
        # fanendtimevalue = request.get(fanendtimevalue=fanendtimevalue)
        # fanendminutevalue = request.get(fanendminutevalue=fanendminutevalue)

        # doorpower = request.get(doorpower=doorpower)
        # doorstate = request.get(doorstate=doorstate)
        # doortoggle = request.get(doortoggle=doortoggle)
        # doorautotoggle = request.get(doorautotoggle=doorautotoggle)
        # doorstarttimevalue = request.get(doorstarttimevalue=doorstarttimevalue)
        # doorstartminutevalue = request.get(doorstartminutevalue=doorstartminutevalue)
        # doorendtimevalue = request.get(doorendtimevalue=doorendtimevalue)
        # doorendminutevalue = request.get(doorendminutevalue=doorendminutevalue)
    
        # waterlevelwarning = request.get(waterlevelwarning=waterlevelwarning)
        # watertempwarning = request.get(watertempwarning=watertempwarning)
        # tempwarning = request.get(tempwarning=tempwarning)
        # humwarning = request.get(humwarning=humwarning)
        # soilwarning = request.get(soilwarning=soilwarning)