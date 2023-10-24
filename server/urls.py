from django.urls import path
from .views import DoorView, FanView, InfoView, LedView, RaspberryView, WarningView, WaterView
from .views import register_smartfarm_view

app_name = 'server'

urlpatterns = [
    # path('', PatentAttorneyListView.as_view(), name='patent-attorney-list'),
    # path('<int:pk>/', PatentAttorneyRetrieveView.as_view(), name='patent-attorney-retrieve')
    path('raspberry', RaspberryView.as_view()),
    path('info', InfoView.as_view()),
    path('led', LedView.as_view()),
    path('water', WaterView.as_view()),
    path('fan', FanView.as_view()),
    path('door', DoorView.as_view()),
    path('warning', WarningView.as_view()),
    path("register/smartfarm", register_smartfarm_view, name="register-smartfarm")
]

