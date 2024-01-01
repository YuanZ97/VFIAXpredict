from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('database', views.ValuesViewSet)

urlpatterns = [
    path('firsttemp', views.first_temp),
    path('', include(router.urls))
]