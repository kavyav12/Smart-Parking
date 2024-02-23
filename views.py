from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import ParkingSlot
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have been successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')
def parking_availability(request):
    parking_slots = ParkingSlot.objects.all()
    return render(request, 'parking_availability.html', {'parking_slots': parking_slots})

def payment(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'payment.html')

def register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')
            if password == confirm_password:
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username=username, password=password)
                    auth_login(request, user)
                    messages.success(request, 'You have been successfully registered and logged in!')
                    return redirect('home')
                else:
                    messages.error(request, 'Username already exists. Please choose a different one.')
            else:
                messages.error(request, 'Passwords do not match. Please try again.')
        return render(request, 'register.html')
def pre_booking(request):
    return render(request, 'pre_booking.html')

def pre_booking_submit(request):
    if request.method == 'POST':
        return redirect('payment')
    else:
        pass