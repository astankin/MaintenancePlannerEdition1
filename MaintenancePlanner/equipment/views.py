from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django_filters.views import FilterView

from MaintenancePlanner.accounts.mixins import AllowedUsersMixin

from MaintenancePlanner.equipment.filters import EquipmentFilter
from MaintenancePlanner.equipment.forms import EquipmentForm
from MaintenancePlanner.equipment.models import Equipment


class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    context_object_name = 'equipment'
    template_name = 'equipment_list.html'
    paginate_by = 12

    def get_queryset(self):
        order_by_param = self.request.GET.get('order_by')
        default_ordering = 'id'
        valid_ordering_fields = ['description', 'type', 'acquisition_date', 'acquisition_value', 'year_of_manufacture']
        ordering = order_by_param if order_by_param in valid_ordering_fields else default_ordering
        return Equipment.objects.order_by(ordering)


@login_required()
def view_equipment(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    return HttpResponseRedirect(reverse('home-page'))


class CreateEquipment(LoginRequiredMixin, AllowedUsersMixin, CreateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    template_name = 'create-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


class UpdateEquipment(LoginRequiredMixin, AllowedUsersMixin, UpdateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    template_name = 'edit-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


class DeleteEquipment(LoginRequiredMixin, AllowedUsersMixin, DeleteView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    success_url = reverse_lazy('equipment-list')


def search_equipment(request):
    if request.method == "POST":
        number = request.POST['number']
        try:
            equipment = Equipment.objects.filter(pk=number)
        except:
            return render(request, 'exception.html')

        context = {
            'number': number,
            'equipment': equipment
        }
        return render(request, 'search-equipment.html', context)
    else:
        return render(request, 'search-equipment.html', {})


def advanced_search_equipment(request):
    equipment = Equipment.objects.all()
    eq_filter = EquipmentFilter(request.GET, queryset=equipment)
    equipment = eq_filter.qs
    context = {
        "eq_filter": eq_filter,
        "equipment": equipment,
    }

    return render(request, 'advanced-search-equipment.html', context)