
from django.contrib import admin
from django.urls import path
from medapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('Departments/', views.Departments , name='Departments'),
    path('Doctors/', views.Doctors, name='Doctors'),
]
