from django.contrib import admin
from meseros.models import Meseros


@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'procedencia')
    list_filter = ('nombre',)