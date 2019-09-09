from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='todoHome'),
    path('add', views.add_todo,name='todo-add'),
    path('deleteCompleted', views.deleteCompleted,name='deleteCompleted'),
    path('deleteAll', views.deleteAll,name='deleteAll'),
    path('edit/<int:todo_id>', views.edit_todo,name='todo-edit'),
    path('detail/<int:todo_id>', views.details_todo,name='todo-detail'),
    path('cross_off/<int:todo_id>', views.cross_off,name='cross-off'),
    path('uncross/<int:todo_id>', views.uncross,name='uncross'),
]
