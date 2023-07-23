from django import forms
from django_countries.widgets import CountrySelectWidget

from MaintenancePlanner.plant.models import Plant, Department
from django_countries.fields import CountryField


class PlantCreateForm(forms.ModelForm):
    country = CountryField().formfield(widget=CountrySelectWidget(attrs={"class": "form-control"}))

    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_center': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'plant': forms.Select(attrs={'class': 'form-control'}),
        }
