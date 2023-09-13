from django.urls import path
from . import views

urlpatterns = [
    path('admindash/', views.index, name='home'),
    path('admindash/category', views.offre_fetch, name='offre'),
]
