from django.contrib import admin
from Tourpackageapp.models import Package, Packager
from Tourpackageapp.models import Bus

# Register your models here.
admin.site.register(Packager)
admin.site.register(Package)
admin.site.register(Bus)