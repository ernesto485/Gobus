from django import forms
from .models import Autobus, Ruta, Conductor


class AutobusForm(forms.ModelForm):
    class Meta:
        model = Autobus
        fields = ['matricula', 'capacidad', 'modelo']
        widgets = {
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ABC-1234',
                'required': True
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 45',
                'min': '1',
                'required': True
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Mercedes-Benz Sprinter',
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' modern-input'


class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'paradas', 'distancia', 'autobus', 'conductor', 'hora_salida', 'frecuencia']
        widgets = {
            'origen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Madrid',
                'required': True
            }),
            'destino': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Barcelona',
                'required': True
            }),
            'paradas': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ["Zaragoza", "Lérida"]',
                'rows': 3,
                'help_text': 'Lista de paradas intermedias en formato JSON'
            }),
            'distancia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 620',
                'step': '0.1',
                'min': '0.1',
                'required': True
            }),
            'autobus': forms.Select(attrs={
                'class': 'form-control',
                'required': False
            }),
            'conductor': forms.Select(attrs={
                'class': 'form-control',
                'required': False
            }),
            'hora_salida': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'required': True
            }),
            'frecuencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Diario, Semanal, Cada 30 min',
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' modern-input'
        
        # Filtrar solo autobuses y conductores activos si es necesario
        self.fields['autobus'].queryset = Autobus.objects.all()
        self.fields['autobus'].empty_label = "-- Sin autobus asignado --"
        
        self.fields['conductor'].queryset = Conductor.objects.all()
        self.fields['conductor'].empty_label = "-- Sin conductor asignado --"
