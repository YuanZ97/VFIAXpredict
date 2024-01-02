from django.urls import path, include
from .views import first_temp, Update_Db, ValuesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('database', ValuesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('firsttemp', first_temp),
    path('answer/', Update_Db.as_view(), name='scraped-data'),
]