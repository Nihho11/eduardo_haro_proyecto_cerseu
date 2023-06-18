from django.urls import path
from . import views

urlpatterns = [
    path('meseros/list/', views.meseros_list, name='meseros_list'),
    # VBC:
    path('meseros_list_vc', views.MeserosList.as_view(), name="meseros_list_vc"),
    path('meseros_create_vc', views.MeserosCreate.as_view(), name="meseros_create_vc"),
    path('meseros_update_vc/<int:pk>', views.MeserosUpdate.as_view(), name="meseros_update_vc"),
    path('meseros_delete_vc/<int:pk>', views.MeserosDelete.as_view(), name="meseros_delete_vc"),
    # URLs serializers
    path('meseros_list_serializer', views.ListMeserosSerializer, name="meseros_list_ssr"),

    # URLs DRF
    path('meseros_list_drf_def/', views.meseros_api_view, name="meseros_list_drf_def"),
    path('meseros_detail_drf_def/<int:pk>', views.meseros_details_view, name="meseros_detail_drf_def")
    ]