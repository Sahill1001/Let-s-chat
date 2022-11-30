from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('save-user', views.saveuser, name='saveuser'),
    path('room', views.room, name='room'),
    path('data', views.data, name='data'),
]