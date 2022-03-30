from django.urls import path
from . import views

urlpatterns = [
    path('clients/test/', views.index),
    path('clients/auth_login/', views.auth_login),
    path('clients/create/', views.create),
    path('clients/auth_info/', views.auth_info),
    path ('clients/<int:user_id>/match/', views.match),
    path ('clients/<int:user_id>/match/like/', views.set_like),
    path ('clients/<int:user_id>/match/dislike/', views.set_dislike),
    path('list/', views.users_list),
    path('distance/<int:distance>', views.list_distance)
]
