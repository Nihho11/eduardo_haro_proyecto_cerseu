from django.urls import path
from . import views

urlpatterns = [
    path('platos/list/', views.platos_list, name='platos_list'),
    # Serializer
    path('platos_list_serializer', views.ListPlatosSerializer, name="platos_list_ssr"),
    # URLs DRF
    path('platos_list_drf_def/', views.platos_api_view, name="platos_list_drf_def"),
    path('platos_detail_drf_def/<int:pk>', views.platos_details_view, name="platos_detail_drf_def")
    ]
