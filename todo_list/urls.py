from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='display'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
]