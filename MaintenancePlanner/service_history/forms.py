from django import forms

from MaintenancePlanner.service_history.models import ServiceHistory


class ServiceHistoryForm(forms.ModelForm):
    class Meta:
        model = ServiceHistory
        exclude = ('created_at', 'technician')

        widgets = {
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'solution': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }


class ServiceHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceHistory
        exclude = ('equipment', 'created_at', 'technician')

        widgets = {
            'problem_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'solution': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
        }
