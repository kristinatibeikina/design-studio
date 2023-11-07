from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    url('application_list/', views.ApplicationListView.as_view(), name='application_list'),
    path('logout/', views.logout, name='logout'),
    path('main_request/', views.ApplicationCreate.as_view(), name='main_request'),
    path('request/', views.MyPostListViews.as_view(), name='user_posts'),
    path('application/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application_delete'),
    path('admin_base/', views.ApplicationListViewAdmin.as_view(), name='admin_list'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('category_do/', views.CategoryCreate.as_view(), name='category_do'),
    path('change/<int:pk>/status/', views.ChangeStatusRequest.as_view(), name='change_status'),
]
