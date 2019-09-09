from django.urls import path
from . import views

urlpatterns = [
    path('', views.home4, name='home4'),
    path('add/', views.add_album, name='add-album'),
    path('details/<int:pk>', views.album_detail, name='album_detail'),
    path('edit/<int:pk>', views.edit_album, name='edit_album'),
    path('delete/<int:pk>', views.delete_diary, name='delete_diary'),
]
