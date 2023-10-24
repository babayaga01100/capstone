from django.urls import path
from .views import register_crop_view, modify_crop_view, remove_crop_view

app_name = 'crops'

urlpatterns = [
    path('register/crop', register_crop_view, name='register-crop'),
    path('modify/crop', modify_crop_view, name='modify-crop'),
    path('delete/crop', remove_crop_view, name='delete-crop'),
    # path('image', .as_view()),
    # path('ndvi', .as_view()),
]

