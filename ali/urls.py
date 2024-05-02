"""
URL configuration for ali project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('sginup/', views.sginup, name='sginup'),
    path('index/', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('groups/', views.groups, name='groups'),
    path('profile/', views.profile, name='profile'),
    path('rounder/', views.rounder, name='rounder'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('values/', views.values, name='values'),
    path('testimnal/', views.testimnal, name='testimnal'),
    path('get_data/', views.get_serial_data, name='get_data'),
    path('image/', views.image, name='image'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
