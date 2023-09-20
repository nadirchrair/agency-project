from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admindash/', views.index, name='home'),
    path('admindash/category', views.offre_fetch, name='offre'),
    path('admindash/category/add', views.add_ofrre, name='add_ofrre'),
    path('admindash/category/<int:id>', views.offre_details, name='offre_details'),
    path('admindash/category/update/<int:id>', views.updateoffre, name='updateoffre'),
    path('admindash/category/delete/<int:id>', views.deleteoffre, name='deleteoffre'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line    
]
