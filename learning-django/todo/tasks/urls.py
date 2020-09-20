from django.urls import path
from .views import index, updateTask, deleteTask

urlpatterns = [
    path('', index, name="list"),
    path('update_task/<str:pk>', updateTask, name="update_task"),
]
