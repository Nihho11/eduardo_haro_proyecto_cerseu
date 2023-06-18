from django.forms import ModelForm
from apps.platos.models import Platos


class PlatosForm(ModelForm):
    class Meta:
        model = Platos
        fields = ('nombre', 'precio', 'procedencia',)