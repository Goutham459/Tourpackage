from django.db import models
from django.contrib.auth.models import User


class Packager(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/packagers", null=True, blank=True)

    def __str__(self):
        return self.name

class Bus(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    image1 = models.ImageField(upload_to="images/bus", null=True, blank=True)
    image2 = models.ImageField(upload_to="images/bus", null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=20,null=True, blank=True)
    contact = models.CharField(max_length=20,null=True, blank=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name



class Package(models.Model):
    place = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="images/packages", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    packager = models.ForeignKey(Packager, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="images/packages", null=True, blank=True)
    image2 = models.ImageField(upload_to="images/packages", null=True, blank=True)
    image3 = models.ImageField(upload_to="images/packages", null=True, blank=True)
    pdf = models.FileField(upload_to="pdf/packages",  null=True, blank=True)

    def __str__(self):
        return self.place





