from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('backend/', include('backend.urls')),
    path('admin/', admin.site.urls),
]