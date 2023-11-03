from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    url('application/', views.ApplicationListView.as_view(), name='application'),
    path('logout/', views.logout, name='logout'),
]
