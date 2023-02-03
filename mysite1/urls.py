"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', views.dashboard, name='dashboard'),
    # path('', views.login, name='login'),
    path('login/', views.handeLogin, name='login'),
    path('logout/', views.handelLogout, name='logout'),
    path('challan/', views.challan, name='challan'),
    path('jobsheet/', views.jobsheet, name='jobsheet'),
    path('product/', views.product, name='product'),
    path('customer/', views.customer, name='customer'),
    path('savecustomer/', views.savecustomer, name='savecustomer'),
    path('teams/', views.teams, name='teams'),
    path('jobstatus/', views.jobstatus, name='jobstatus'),
    path('addnewchallan/', views.addnewchallan, name='addnewchallan'),
    path('updatechallan/<int:pk>/', views.updatechallan, name='updatechallan'),
    path('deletechallan/<int:pk>/', views.deletechallan, name='deletechallan'),
    # path('challan/get_more_tables/', views.get_more_tables, name='get_more_tables'),
]

# export DJANGO_SETTINGS_MODULE=mysite.settings
