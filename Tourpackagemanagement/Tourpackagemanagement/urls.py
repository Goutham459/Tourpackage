"""
URL configuration for Tourpackagemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from Tourpackageapp import views
from Tourpackagemanagement import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('packagers/', views.packagers, name='packagers'), 
    path('packages/<str:name>/', views.packages, name="packages"),
    path('packagedetails/<int:pk>/', views.packagedetails, name='packagedetails'),
    path('bus/',views.bus,name='bus'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name="login"),
    path('logout/', views.signout, name='logout'),
    path('enquiry/',views.enquiry,name="enquiry"),
     path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('password_reset_verify/<str:email>/', views.password_reset_verify, name='password_reset_verify'),
    path('password_reset_new/<str:email>/', views.password_reset_new, name='password_reset_new'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)