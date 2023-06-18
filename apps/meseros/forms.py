from django.forms import ModelForm
from apps.meseros.models import Meseros


class MeserosForm(ModelForm):
    class Meta:
        model = Meseros
        fields = ('nombre', 'nacionalidad', 'procedencia', 'edad')
