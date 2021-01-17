from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views import View


def index(request):
    user = request.user
    context = {user,}
    return render(request, 'registration/login.html', context)

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            messages.info(request, "Błąd logowania. Spróbuj ponownie.")
    return render(request, 'registration/login.html')


@login_required
def home(request):
    return render(request, 'index.html')



class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
