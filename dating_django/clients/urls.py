from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('auth_login/', views.auth_login),
    path('create/', views.create),
    path('auth_info/', views.auth_info),
    path ('<int:user_id>/match/', views.match),
    path ('<int:user_id>/match/like/', views.set_like),
    path ('<int:user_id>/match/dislike/', views.set_dislike),
]
