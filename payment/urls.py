from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('webhook', views.webhook, name='stripe-webhook'),
]