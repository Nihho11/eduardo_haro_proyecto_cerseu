from django.urls import path
from . import views

urlpatterns = [
    path('meseros/list/', views.meseros_list, name='meseros_list')
    ]