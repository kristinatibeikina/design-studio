from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('registration/', views.registration, name='registration'),
]
