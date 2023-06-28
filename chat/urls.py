from django.urls import path

from . import views
from .views import Home
app_name = 'chat'
urlpatterns = [
    # path('origin/', Home.as_view(), name='index'),
    path('', views.index, name='index'),
    path('main/', views.room, name='room'),
    path('<str:room_name>/', views.room, name='room'),


]
