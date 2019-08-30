from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home-Page'),
    path('about/', views.about, name='First-Page'),
]