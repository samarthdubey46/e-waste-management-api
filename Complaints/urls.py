from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ComplaintsView, counter, create

app_name = 'Complaints'
router = DefaultRouter()
router.register('', ComplaintsView, basename='ComplaintViewSet')
urlpatterns = [
    path('counter/', counter),
    path('add/', create),
    path('', include(router.urls)),

]
