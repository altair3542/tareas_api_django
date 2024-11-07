from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.tarea_list_create, name='tarea-list-create'),
    path('tareas/<int:pk>/', views.tarea_detail_update_delete, name='tarea-detail-update-delete'),
]
