from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def index(request):
    user = request.user
    context = {user,}
    return render(request, 'registration/login.html', context)


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def error_page(request):
    return render(request, '404.html')

@login_required
def table_page(request):
    return render(request, 'tables.html')

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
def mylogout(request):
    logout(request)
    return redirect("home")

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Hasło poprawnie zmienione!')
            return redirect('password_change')
        else:
            messages.error(request, 'Wystąpił błąd.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form})



