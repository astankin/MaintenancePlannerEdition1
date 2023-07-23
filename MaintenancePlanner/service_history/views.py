from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.service_history.forms import ServiceHistoryForm
from MaintenancePlanner.service_history.models import ServiceHistory


class CreateServiceReport(LoginRequiredMixin, CreateView):
    model = ServiceHistory
    template_name = 'create-service-report.html'
    form_class = ServiceHistoryForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.technician = self.request.user
        return super().form_valid(form)


@login_required
def service_history(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    reports = ServiceHistory.objects.filter(equipment=equipment)
    context = {
        'equipment': equipment,
        'reports': reports,
    }
    return render(request, 'service-history.html', context)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = ServiceHistory
    template_name = 'service-history.html'


class ReportEditView(LoginRequiredMixin, UpdateView):
    model = ServiceHistory
    template_name = 'edit-report.html'
    fields = '__all__'
    success_url = reverse_lazy('equipment-list')
