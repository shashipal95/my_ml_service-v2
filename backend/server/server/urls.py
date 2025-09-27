# backend/server/server/urls.py
from django.contrib import admin
from django.urls import path, include  # use include from django.urls

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Add your app endpoints
urlpatterns += endpoints_urlpatterns
