from django import forms
from MaintenancePlanner.equipment.models import Equipment


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('last_checked_date', 'next_check_date')

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'acquisition_date': forms.DateInput(format="%d/%m/%Y", attrs={'class': 'form-control', 'type': 'date'}),
            'currency_code': forms.Select(attrs={'class': 'form-control'}),
            'acquisition_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'plant': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'year_of_manufacture': forms.NumberInput(attrs={'class': 'form-control'}),

        }
