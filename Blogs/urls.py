from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet

router = DefaultRouter()
router.register('', BlogViewSet)

app_name = 'Blogs'
urlpatterns = [
    path('', include(router.urls)),
]
