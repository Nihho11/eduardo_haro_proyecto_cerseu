from django.shortcuts import render
from django.db.models import F, Q
from meseros.models import Meseros


def meseros_list(request):
    query = Q(procedencia='Perú') & Q(edad__lte=30)
    # aumentar la edad 5 años a todos los meseros
    # Meseros.objects.update(edad=F('edad')-5)
    data_context = Meseros.objects.filter(query)
    return render(request, 'meseros/meseros_list.html', context={'data': data_context})

