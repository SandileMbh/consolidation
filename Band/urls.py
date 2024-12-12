from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

"""
URL configuration for the band website, mapping URLs to their respective view functions.

Each URL pattern is associated with a specific view, allowing users to navigate
between pages on the site (home, about, events, login, logout and register).
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('login/', auth_views.LoginView.as_view(template_name='Band/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Band/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
