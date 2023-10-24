from urllib import response
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import SmartFarmCrop
from accounts.models import User
from server.models import SmartFarm

# Create your views here.

# 작물 등록      
@api_view(['POST'])
def register_crop_view(request):
    # 사용자 가져오기
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response({'message': '등록되어 있지 않은 사용자입니다.'}, status=404)
    
    # 스마트팜 가져오기
    try:
        smartfarm = SmartFarm.objects.get(user=user)
    except SmartFarm.DoesNotExist:
        return response({'message': '등록된 스마트팜이 없습니다.'}, status=400)
    
    # 작물 등록하기
    name = request.data['name']
    day = request.data['day']
    crop = SmartFarmCrop.objects.create(name=name, day=day)
    crop.save()
    
    # 스마트팜에 작물 등록하기
    smartfarm.crop = crop
    smartfarm.save()
    
    return Response(status=200)


# 작물 수정
@api_view(['PUT'])
def modify_crop_view(request):
    # 작물 가져오기
    try:
        id = request.data['id']
        name = request.data['name']
        day = request.data['day']
        
        crop = SmartFarmCrop.objects.get(id=id)
        crop.name = name
        crop.day = day
        crop.save()
        
        return Response(status=200)
    
    except SmartFarmCrop.DoesNotExist:
        return Response({'message': '작물이 등록되어 있지 않습니다.'}, status=404)    


# 작물 삭제    
@api_view(['DELETE'])
def remove_crop_view(request):
    # 사용자 가져오기
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response({'message': '등록되어 있지 않은 사용자입니다.'}, status=404)
    
    # 스마트팜 가져오기
    try:
        smartfarm = SmartFarm.objects.get(user=user)
    except SmartFarm.DoesNotExist:
        return response({'message': '등록된 스마트팜이 없습니다.'}, status=400)
    
    # 작물 삭제하기
    try:
        id = request.data['id']
        smartfarm = SmartFarmCrop.objects.get(id=id)
        smartfarm.delete()
        
        return Response(status=200)
    except SmartFarmCrop.DoesNotExist:
        return Response({'message': '등록되어 있지 않은 스마트팜입니다.'}, status=404)
    
# 작물 이미지 보내기
# class RaspberryView(APIView):