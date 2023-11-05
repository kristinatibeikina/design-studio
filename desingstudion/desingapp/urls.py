from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    url('application_list/', views.ApplicationListView.as_view(), name='base'),
    path('logout/', views.logout, name='logout'),
    path('main_request/', views.ApplicationCreate.as_view(), name='main_request'),
    path('request/', views.MyPostListViews.as_view(), name='user_posts'),
]
