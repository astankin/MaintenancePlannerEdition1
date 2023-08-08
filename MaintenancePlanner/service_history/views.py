from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.service_history.forms import ServiceHistoryForm, ServiceHistoryUpdateForm
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


# class ReportEditView(LoginRequiredMixin, UpdateView):
#     model = ServiceHistory
#     template_name = 'edit-report.html'
#     form_class = ServiceHistoryUpdateForm
#
#     def get_success_url(self):
#         equipment_id = self.object.equipment.id
#         return reverse_lazy('service-history', kwargs={'pk': equipment_id})


class ReportEditView(LoginRequiredMixin, UpdateView):
    model = ServiceHistory
    template_name = 'edit-report.html'
    form_class = ServiceHistoryUpdateForm

    def get_success_url(self):
        equipment_id = self.object.equipment.id
        return reverse_lazy('service-history', kwargs={'pk': equipment_id})

    def get(self, request, *args, **kwargs):
        report = self.get_object()
        if report.technician != self.request.user:
            return render(request, 'no-permission.html',)

        return super().get(request, *args, **kwargs)
