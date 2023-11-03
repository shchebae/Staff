from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rasp', views.rasp, name='rasp'),
    path('create', views.create, name='create'),
]
