"""MySqLBootstrapCsv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from search_up.views import home, mylogin, password_change, mylogout, table_page, error_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mylogin, name='login'),
    path('logout/', mylogout, name='logout'),
    path('account/password_change/', password_change, name='password_change'),

    path('home/', home, name='home'),
    path('table_page/', table_page, name='table_page'),
    path('error_page/', error_page, name='error_page'),

]