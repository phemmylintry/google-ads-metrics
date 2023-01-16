from django.contrib import admin
from django.urls import path
from ads.views import calculate_metrics

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", calculate_metrics),
]
