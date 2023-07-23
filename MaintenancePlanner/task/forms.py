from django import forms

from MaintenancePlanner.accounts.models import AppUser
from MaintenancePlanner.task.models import Task


class CreateTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['technician'].queryset = AppUser.objects.filter(role='OPERATOR')

    class Meta:
        model = Task
        exclude = ('complete', 'equipment')
        widgets = {
            'technician': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'created_on': forms.DateInput(format="%d/%m/%Y", attrs={'class': 'form-control', 'type': 'date'}),

        }


# class DisabledFormMixin:
#     disabled_fields = ()
#     fields = {}
#
#     def _disable_fields(self):
#         if self.disabled_fields == '__all__':
#             fields = self.fields.keys()
#         else:
#             fields = self.disabled_fields
#
#         for fields_name in fields:
#             if fields_name in self.fields:
#                 field = self.fields[fields_name]
#                 field.widget.attr['disabled'] = 'disabled'
#                 field.widget.attr['readonly'] = 'readonly'


class UserUpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('complete',)

        labels = {
            'complete': 'Mark as completed: '
        }

        widgets = {
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': "checkbox",
                'id': 'flexCheckDefault',
            }),

        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'technician', 'equipment', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'technician': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
