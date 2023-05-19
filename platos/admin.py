from django.contrib import admin
from platos.models import Platos


@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('nombre',)