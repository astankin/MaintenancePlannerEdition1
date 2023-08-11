from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView, TemplateView

from MaintenancePlanner.accounts.decorators import allowed_users
from MaintenancePlanner.accounts.mixins import AllowedUsersMixin
from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.maintenance_plan.forms import CreateMaintenancePlanForm, CreateOperationForm, \
    UpdateOperationForm, MaintenancePlanForm
from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel, Operation


@login_required
@allowed_users(allowed_roles=['MANAGER', 'SUPERVISOR'])
def create_mp(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateMaintenancePlanForm(request.POST)
        if form.is_valid():
            mp = form.save(commit=False)
            mp.equipment = equipment
            mp.save()
            return redirect(reverse('mp-details', kwargs={'pk': mp.id}))
    else:
        form = CreateMaintenancePlanForm()
    context = {
        'form': form,
        'equipment': equipment,
    }
    return render(request, 'mp/create-mp.html', context)


class CreateMPView(LoginRequiredMixin, AllowedUsersMixin, CreateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = MaintenancePlanModel
    form_class = MaintenancePlanForm
    template_name = 'mp/create-mp.html'
    success_url = reverse_lazy('mp-created-success')


@login_required
def mp_details(request, pk):
    mp = MaintenancePlanModel.objects.get(pk=pk)
    operations = Operation.objects.filter(maintenance_plan=mp)
    context = {
        'mp': mp,
        'operations': operations,
    }
    return render(request, 'mp/maintenance-plan.html', context)


class DeleteMP(LoginRequiredMixin, AllowedUsersMixin, DeleteView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = MaintenancePlanModel
    success_url = reverse_lazy('equipment-list')


@login_required
@allowed_users(allowed_roles=['MANAGER', 'SUPERVISOR'])
def create_operation(request, pk):
    mp = MaintenancePlanModel.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateOperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            operation.maintenance_plan = mp
            operation.save()
            return redirect(reverse('mp-details', kwargs={'pk': pk}))
    else:
        form = CreateOperationForm()

    context = {
        'form': form,
        'mp': mp,
    }
    return render(request, 'operation/create-operation.html', context)


class UpdateOperation(LoginRequiredMixin, AllowedUsersMixin, UpdateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Operation
    form_class = UpdateOperationForm
    template_name = 'operation/update-operation.html'

    def get_success_url(self):
        return reverse('mp-details', kwargs={
            'pk': self.object.maintenance_plan.pk
        })


class OperationDetail(LoginRequiredMixin, DetailView):
    model = Operation
    template_name = 'operation/operation-details.html'


@login_required()
@allowed_users(allowed_roles=['MANAGER', 'SUPERVISOR'])
def delete_operation(request, pk):
    operation = Operation.objects.get(pk=pk)
    mp = operation.maintenance_plan
    if request.method == 'POST':
        operation.delete()
        return redirect(reverse('mp-details', kwargs={'pk': mp.id}))


class MPCreateSuccessView(TemplateView):
    template_name = 'mp/mp-created-message.html'
