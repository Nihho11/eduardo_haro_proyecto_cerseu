from django.shortcuts import render
from django.db.models import F, Q
from platos.models import Platos


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
