import os
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Tourpackageapp.models import Package
from Tourpackageapp.models import Packager
from Tourpackageapp.models import Bus
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages




# Create your views here.

def home(request):
    packagers = Packager.objects.all()
    return render(request, 'home.html',{'packagers':packagers})

def bus(request):
    buses = Bus.objects.all()
    return render(request,'buses.html', {'buses': buses})

def packagers(request):
    packagers = Packager.objects.all()
    return render(request, 'packagers.html',{'packagers':packagers})

def packages(request, name):
    packager = Packager.objects.get(name=name)
    packages = Package.objects.filter(packager=packager)
    return render(request, 'packages.html', {'packager': packager, 'packages': packages})

def packagedetails(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'packagedetails.html', {'package': package})

def enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('n')
        city = request.POST.get('p')
        email = request.POST.get('e')
        date_of_travel = request.POST.get('d')
        contact_number = request.POST.get('c')

        # Example email sending logic using Django's send_mail
        send_mail(
            'New Enquiry',
            f'Name: {name}\nCity: {city}\nEmail: {email}\nDate of Travel: {date_of_travel}\nContact Number: {contact_number}',
            settings.DEFAULT_FROM_EMAIL,  # Use your default sender email here
            ['gouthamkrishancs1@gmail.com'],  # List of recipient(s)
            fail_silently=False,
        )

        return HttpResponse('Enquiry submitted successfully. Thank you!')
    
    return render(request, 'enquiry.html')
        


def login(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')



def signup(request):
    if request.method == "POST":
        n = request.POST.get('n')
        e = request.POST.get('e')
        u = request.POST.get('u')
        p = request.POST.get('p')  # Corrected name attribute to match the form

        # Basic validation
        if not all([n, e, u, p]):
            messages.error(request, 'All fields are required.')
            return redirect('signup')

        # Check if username or email already exists
        if User.objects.filter(username=u).exists() and User.objects.filter(email=e).exists():
            messages.error(request, 'Username and Email are already taken.')
            return redirect('signup')

        if User.objects.filter(username=u).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        if User.objects.filter(email=e).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=u, email=e, password=p, first_name=n)
        messages.success(request, 'Account created successfully. You can now login.')
        return redirect('login')

    return render(request, 'signup.html')
    
@login_required
def signout(request):
    logout(request)
    return redirect('home')


