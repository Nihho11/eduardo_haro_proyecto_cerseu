from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers as ssr
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.meseros.forms import MeserosForm
from apps.meseros.models import Meseros
from apps.meseros.serializers import MeserosSerializer


def meseros_list(request):
    query = Q(procedencia='Perú') & Q(edad__lte=30)
    # aumentar la edad 5 años a todos los meseros
    # Meseros.objects.update(edad=F('edad')+5)
    data_context = Meseros.objects.filter(query)
    return render(request, 'meseros/meseros_list.html', context={'data': data_context})


"""Crear y configurar adecuadamente usando vistas basadas en clases la url,
view y plantilla para crear y otro para listar todos los meseros que sea de
procedencia de Perú"""


class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros/meseros_list_vc.html'


class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros_create.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros/meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list_vc')


class MeserosDelete(DeleteView):
    model = Meseros
    success_url = reverse_lazy('meseros_list_vc')
    template_name = 'meseros/meseros_confirm_delete.html'


def ListMeserosSerializer(request):
    lista_meseros = ssr.serialize('json', Meseros.objects.filter(precio__gte=50),
                                 fields=['nombre', 'nacionalidad', 'procedencia', 'edad'])

    return HttpResponse(lista_meseros, content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def meseros_api_view(request):
    if request.method == 'GET':
        print("Ingresó a GET")
        queryset = Meseros.objects.all()
        serializers_class = MeserosSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print("Data meseros: {}".format(request.data))
        serializer_class = MeserosSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)


@api_view(['GET', 'PUT', 'DELETE'])
def meseros_details_view(request, pk):
    meseros = Meseros.objects.filter(id=pk).first()
    if meseros:
        if request.method == 'GET':
            print("Ingresó a GET")
            serializers_class = MeserosSerializer(meseros)
            return Response(serializers_class.data)

        elif request.method == 'PUT':
            serializer_class = MeserosSerializer(meseros, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            meseros.delete()
            return Response('Mesero ha sido eliminado correctamente de la base de datos', status=status.HTTP_200_OK)