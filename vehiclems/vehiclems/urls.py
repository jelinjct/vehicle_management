
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', TemplateView.as_view(template_name='vehicle_management/profile.html'), name='profile'),
    path('', include('vehicle_management.urls')),
    path('user/', include('user_access.urls')),
]
