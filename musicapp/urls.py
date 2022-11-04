from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteList, ArtisteDetail, SongList, SongDetail, LyricList, LyricDetail



urlpatterns = [
    path('artistes/', ArtisteList.as_view()),
    path('artistes/<int:pk>/', ArtisteDetail.as_view()),
    path('songs/', SongList.as_view()),
    path('songs/<int:pk>/', SongDetail.as_view()),
    path('lyrics/', LyricList.as_view()),
    path('lyrics/<int:pk>/', LyricDetail.as_view()),
]
