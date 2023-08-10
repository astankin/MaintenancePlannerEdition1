from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('MaintenancePlanner.common.urls')),
                  path('equipment/', include('MaintenancePlanner.equipment.urls')),
                  path('user/', include('MaintenancePlanner.accounts.urls')),
                  path('plant/', include('MaintenancePlanner.plant.urls')),
                  path('mp/', include('MaintenancePlanner.maintenance_plan.urls')),
                  path('task/', include('MaintenancePlanner.task.urls')),
                  path('service-history/', include('MaintenancePlanner.service_history.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = TemplateView.as_view(template_name='common/404.html')
handler500 = TemplateView.as_view(template_name='common/500.html')
handler400 = TemplateView.as_view(template_name='common/400.html')
