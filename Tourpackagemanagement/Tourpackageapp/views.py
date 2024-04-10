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
from django.contrib import messages





# Create your views here.
def home(request):
    packagers = Packager.objects.all()
    return render(request, 'home.html', {'packagers': packagers})

def bus(request):
    buses = Bus.objects.all()
    return render(request,'buses.html', {'buses': buses})

def packagers(request):
    packagers = Packager.objects.all()
    return render(request, 'home.html',{'packagers':packagers})

def packages(request, name):
    packager = Packager.objects.get(name=name)
    packages = Package.objects.filter(packager=packager)
    return render(request, 'packages.html', {'packager': packager, 'packages': packages})

def packagedetails(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'packagedetails.html', {'package': package})

def enquiry(request):
    return render(request,'enquiry.html')


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
        p = request.POST.get('p')

        # Basic validation
        if not all([n, e, u, p]):
            messages.error(request, 'All fields are required.')
            return redirect('signup')

        if User.objects.filter(username=u).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        if User.objects.filter(email=e).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')


        user = User.objects.create_user(username=u, email=e, password=p, first_name=n)
        messages.success(request, 'Account created successfully. You can now login.')
        return redirect('login')

    else:
        return render(request, 'signup.html')

