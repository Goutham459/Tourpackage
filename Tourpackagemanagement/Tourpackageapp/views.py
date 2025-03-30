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
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render




# Create your views here.

def home(request):
    packagers = Packager.objects.all()
    return render(request, 'home.html',{'packagers':packagers})

def about(request):
    return render (request,'about.html')

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


@login_required
def enquiry(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('n')
            city = request.POST.get('p')
            email = request.POST.get('e')
            date_of_travel = request.POST.get('d')
            contact_number = request.POST.get('c')

            # Sending the email
            send_mail(
                'New Enquiry',
                f'Name: {name}\nCity: {city}\nEmail: {email}\nDate of Travel: {date_of_travel}\nContact Number: {contact_number}',
                settings.EMAIL_HOST_USER,
                ['gouthamkrishnacs1@gmail.com'], 
                fail_silently=False,
            )

            return JsonResponse({'message': 'Your enquiry has been submitted successfully!'})
        except Exception as e:
            return JsonResponse({'message': 'There was a problem submitting your enquiry. Please try again.'}, status=500)

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
        p = request.POST.get('p')

        if not all([n, e, u, p]):
            messages.error(request, 'All fields are required.')
            return redirect('signup')

        if User.objects.filter(username=u).exists() and User.objects.filter(email=e).exists():
            messages.error(request, 'Username and Email are already taken.')
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

    return render(request, 'signup.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

otp_storage = {}

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            otp = get_random_string(length=6, allowed_chars='0123456789')
            otp_storage[email] = otp
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'OTP has been sent to your email.')
            return redirect('password_reset_verify', email=email)
        else:
            messages.error(request, 'Email not found.')
    return render(request, 'password_reset_request.html')

def password_reset_verify(request, email):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp_storage.get(email) == otp:
            del otp_storage[email]
            return redirect('password_reset_new', email=email)
        else:
            messages.error(request, 'Invalid OTP.')
    return render(request, 'password_reset_verify.html', {'email': email})

def password_reset_new(request, email):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Password has been reset successfully.')
        return redirect('login')
    return render(request, 'password_reset_new.html', {'email': email})


def terms(request):
    return render(request, 'terms.html')


