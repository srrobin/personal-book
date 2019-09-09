from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='home2'),
    path('add', views.add_diary, name='add-diary'),
    path('detail/<int:diary_id>', views.detail, name='detail-diary'),
    path('edit/<int:diary_id>', views.edit_diary, name='edit-diary'),
    path('delete/<int:diary_id>', views.delete_diary, name='delete-diary'),
]