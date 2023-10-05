from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('search/', views.search, name='search'),
    path('trending/', views.trending, name='trending'),
    path('playlist/', views.playlist, name='playlist'),
    path('usersong/', views.usersong, name='usersong'),
    path('listenlater/', views.listenlater, name='listenlater'),
    path('upload/', views.upload, name='upload'),
    path('creatplaylist/', views.creatplaylist, name='creatplaylist'),
    path('addplaylist/', views.addtoplaylist, name='addplaylist'),
    path('playlists/<int:id>', views.playlistdisplay, name='playlistdetails'),
    path('report/', views.report_song, name='report_song'),
]
