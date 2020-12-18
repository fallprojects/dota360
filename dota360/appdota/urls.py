from django.contrib import admin
from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('heroes/',heroList,name='heroes'),
    path('heroinfo/<str:hero_name>/',heroInfo,name='heroinfo'),
    # path('herobuild/',name='herobuild'),
]
