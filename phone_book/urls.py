from django.urls import path
from . import views

urlpatterns = [
    path('', views.home3, name='home3'),
    path('add', views.add_pn, name='add-pn'),
    path('detail/<int:pn_id>', views.detail_pn, name='detail-pn'),
    path('delete/<int:pn_id>', views.delete_pn, name='delete-pn'),
    path('edit/<int:pn_id>', views.edit_pn, name='edit-pn'),
    path('category', views.category_list, name='category-list'),

]
