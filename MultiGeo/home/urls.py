from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('tutorial/', views.tutorial, name= 'tutorial'),
    path('especificaciones/', views.especificaciones, name= 'especificaciones'),
]