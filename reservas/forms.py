from django import forms
from .models import Cliente, Conductor, Reservacion
from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'ci', 'contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'ci': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '11'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        if not ci.isdigit() or len(ci) != 11:
            raise ValidationError("El CI debe tener exactamente 11 dígitos numéricos.")
        return ci

    def clean_contacto(self):
        contacto = self.cleaned_data.get('contacto')
        if not contacto.isdigit() or len(contacto) != 8:
            raise ValidationError("El contacto debe tener exactamente 8 dígitos numéricos.")
        return contacto

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'apellido', 'contacto', 'ci', 'marca_carro', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'ci': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '11'}),
            'marca_carro': forms.TextInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    def clean_ci(self):
        ci = self.cleaned_data['ci']
        if len(ci) != 11 or not ci.isdigit():
            raise forms.ValidationError("El CI debe tener exactamente 11 dígitos numéricos.")
        return ci

    def clean_contacto(self):
        contacto = self.cleaned_data['contacto']
        if len(contacto) != 8 or not contacto.isdigit():
            raise forms.ValidationError("El número de contacto debe tener exactamente 8 dígitos.")
        return contacto

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['fecha', 'hora', 'destino', 'cliente', 'conductor']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-control'}),
        }
