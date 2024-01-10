from django.urls import path
from . import views
from .views import main
from .views import aboutme
from .views import portfoliome
from .views import contactme

urlpatterns = [
    path('main/', views.main, name="main"),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('portfoliome/', views.portfoliome, name='portfoliome'),
    path('contactme/', views.contactme, name='contactme'),
]