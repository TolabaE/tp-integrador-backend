from django import forms
from .models import MovimientoStock

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['producto', 'cantidad', 'tipo', 'observacion']