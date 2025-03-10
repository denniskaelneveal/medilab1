from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
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

def edit(request,id):
    appointment1 = get_object_or_404(Appointments, id=id)
    if request.method == "POST":
        appointment1.name = request.POST.get('name')
        appointment1.email = request.POST.get('email')
        appointment1.phone = request.POST.get('phone')
        appointment1.date = request.POST.get('date')
        appointment1.department = request.POST.get('department')
        appointment1.doctor = request.POST.get('doctor')
        appointment1.message = request.POST.get('message')
        appointment1.save()
        return redirect('/Show')
    else:
        return render(request,'edit.html',{'appointment1':appointment1})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')




















