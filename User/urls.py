from django.urls import path, include
from .views import *
from knox import views as knox_views

app_name = 'User'

urlpatterns = [
    path('register/', register),
    path('login/', Login.as_view()),
    path('', user),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
