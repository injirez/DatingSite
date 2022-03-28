from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('auth_login/', views.auth_login),
    path('create/', views.create),
    path('auth_info/', views.auth_info)
]