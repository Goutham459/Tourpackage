import os

from django.shortcuts import render, get_object_or_404
from Tourpackageapp.models import Package
from Tourpackageapp.models import Packager
from Tourpackageapp.models import Bus
from django.shortcuts import render





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
        return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

