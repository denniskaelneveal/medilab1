
from django.contrib import admin
from django.urls import path
from medapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/'
         '', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('Departments/', views.Departments , name='Departments'),
    path('Doctors/', views.Doctors, name='Doctors'),
    path('Appointments/', views.Appointments1, name='Appointments'),
    path('Contact/', views.Contact20, name='Contact'),
    path('Show/', views.Show, name='Show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),

]
