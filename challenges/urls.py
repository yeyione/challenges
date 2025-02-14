from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("January", views.january),
    path("february", views.february),
    path("March", views.march),
    
]