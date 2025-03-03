from django.shortcuts import render, redirect
from medapp.models import *
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

def Appointments1(request):
    if request.method == "POST":
        myappointments = Appointments(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointments.save()
        return redirect('/Show')

    else:
        return render(request,'Appointments.html')

def Contact20(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],

        )
        mycontact.save()
        return redirect('/Contact')
    else:
        return render(request,'Contact.html')

def Show(request):
    all = Appointments.objects.all()
    return render(request,'Show.html',{'all':all})

def delete(request,id):
    deleteappointment= Appointments.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/Show')





















