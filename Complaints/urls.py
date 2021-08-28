from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ComplaintsView

app_name = 'Complaints'
router = DefaultRouter()
router.register('', ComplaintsView,basename='ComplaintViewSet')
urlpatterns = [
    path('', include(router.urls)),
]
