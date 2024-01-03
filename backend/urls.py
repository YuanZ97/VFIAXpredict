from django.urls import path, include
from .views import frontend_temp, ValuesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('database', ValuesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('frontend', frontend_temp)
]