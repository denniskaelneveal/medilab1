from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def Departments(request):
    return render(request,'Departments.html')

def Doctors(request):
    return render(request,'Doctors.html')