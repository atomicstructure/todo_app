from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('complete-task/<int:pk>/', views.complete_task, name='complete_task'),
]