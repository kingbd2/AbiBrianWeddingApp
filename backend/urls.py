from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]

urlpatterns += [path('api/v1/silk/', include('silk.urls', namespace='silk'))]
