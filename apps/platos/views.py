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
from apps.platos.models import Platos
from apps.platos.forms import PlatosForm
from apps.platos.serializers import PlatosSerializer


def platos_list(request):
    # p1 = Platos(nombre='Causa Familiar', precio=50, procedencia='Perú')
    # p1.save()
    # p2 = Platos(nombre='Tequeños', precio=24, procedencia='Perú')
    # p2.save()
    # p3 = Platos(nombre='Arepas Grandes', precio=45, procedencia='Venezuela')
    # p3.save()
    query = Q(procedencia='Perú') & Q(precio__gte=40)
    data_context = Platos.objects.filter(query)
    return render(request, 'platos/platos_list.html', context={'data': data_context})


def ListPlatosSerializer(request):
    lista_platos = ssr.serialize('json', Platos.objects.filter(precio__gte=50), fields=['nombre', 'precio', 'procedencia'])

    return HttpResponse(lista_platos, content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def platos_api_view(request):

    if request.method == 'GET':
        print("Ingresó a GET")
        queryset = Platos.objects.all()
        serializers_class = PlatosSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print("Data platos: {}".format(request.data))
        serializer_class = PlatosSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def platos_details_view(request, pk):
    platos = Platos.objects.filter(id=pk).first()
    if platos:
        if request.method == 'GET':
            print("Ingresó a GET")
            serializers_class = PlatosSerializer(platos)
            return Response(serializers_class.data)

        elif request.method == 'PUT':
            serializer_class = PlatosSerializer(platos, data=request.data)

            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            platos.delete()
            return Response('Plato ha sido eliminado correctamente de la base de datos', status=status.HTTP_200_OK)