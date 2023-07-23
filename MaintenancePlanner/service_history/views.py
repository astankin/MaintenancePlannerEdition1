from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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


# class ReportUpdateView(LoginRequiredMixin, UpdateView):
#     model = ServiceHistory
#     template_name = 'update-report.html'
#     form_class = ServiceHistoryUpdateForm
#
#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         user = self.request.user
#         service_report = self.get_object()
#
#         if service_report.technician == user:
#             return response
#         else:
#             raise PermissionDenied("You are not allowed to update this report.")
#
#     def get_success_url(self):
#         equipment_id = self.object.equipment.id
#         return reverse_lazy('service-history', kwargs={'pk': equipment_id})

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceHistory
    template_name = 'update-report.html'
    form_class = ServiceHistoryUpdateForm

    def __init__(self):
        super().__init__()
        self.has_permission = None

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        service_report = self.get_object()

        self.has_permission = service_report.technician == user

        return response

    def get_success_url(self):
        equipment_id = self.object.equipment.id
        return reverse_lazy('service-history', kwargs={'pk': equipment_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_permission'] = self.has_permission
        return context

