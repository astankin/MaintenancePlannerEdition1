from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from MaintenancePlanner.accounts.mixins import AllowedUsersMixin
from MaintenancePlanner.plant.forms import DepartmentCreateForm, PlantCreateForm
from MaintenancePlanner.plant.models import Plant, Department


class PlantCreateView(LoginRequiredMixin, AllowedUsersMixin, CreateView):
    allowed_roles = ['MANAGER']
    template_name = 'plant/create-plant.html'
    model = Plant
    form_class = PlantCreateForm
    success_url = reverse_lazy('plants-list')


class PlantUpdateView(LoginRequiredMixin, AllowedUsersMixin, UpdateView):
    allowed_roles = ['MANAGER']
    model = Plant
    template_name = 'plant/update-plant.html'
    success_url = reverse_lazy('plants-list')
    form_class = PlantCreateForm


class PlantDeleteView(LoginRequiredMixin, AllowedUsersMixin, DeleteView):
    allowed_roles = ['MANAGER']
    model = Plant
    success_url = reverse_lazy('plants-list')
    context_object_name = 'plant'


class PlantListView(LoginRequiredMixin, AllowedUsersMixin, ListView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Plant
    template_name = 'plant/plant-list.html'
    context_object_name = 'plants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants = self.get_queryset()
        departments = {plant.id: plant.department_set.all() for plant in plants}
        context['departments'] = departments
        return context


class DepartmentCreateView(LoginRequiredMixin, AllowedUsersMixin, CreateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    template_name = 'department/create-department.html'
    model = Department
    form_class = DepartmentCreateForm
    success_url = reverse_lazy('department-list')


class DepartmentListVie(LoginRequiredMixin, AllowedUsersMixin, ListView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    template_name = 'department/department-list.html'
    model = Department
    context_object_name = 'departments'


class DepartmentDeleteView(LoginRequiredMixin, AllowedUsersMixin, DeleteView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Department
    success_url = reverse_lazy('department-list')


class DepartmentUpdateView(LoginRequiredMixin, AllowedUsersMixin, UpdateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    template_name = 'department/update-department.html'
    model = Department
    form_class = DepartmentCreateForm
    success_url = reverse_lazy('department-list')
