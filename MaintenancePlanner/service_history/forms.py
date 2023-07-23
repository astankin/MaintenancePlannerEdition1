from django import forms

from MaintenancePlanner.service_history.models import ServiceHistory


class ServiceHistoryForm(forms.ModelForm):
    class Meta:
        model = ServiceHistory
        exclude = ('created_on', 'technician')

        widgets = {
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control'}),
            'solution': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ServiceHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceHistory
        exclude = ('equipment', 'created_on', 'technician')

        widgets = {
            'problem_description': forms.Textarea(attrs={'class': 'form-control'}),
            'solution': forms.Textarea(attrs={'class': 'form-control'}),
        }
