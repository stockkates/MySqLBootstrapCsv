from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views import View


def index(request):
    user = request.user
    context = {user,}
    return render(request, 'registration/login.html', context)


@login_required
def home(request):
    return render(request, 'index.html')

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

    # if request.method == 'POST':
    #     form = PasswordChangeForm(data=request.POST, user=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    #     return redirect('home')
    #     # return render(request, 'registration/password_change_form.html', {'error_notice':error_notice})
    #
    # else:
    #     form = PasswordChangeForm(data=request.POST, user=request.user)
    #     context ={'form':form}
    #     return render(request, 'registration/password_change_form.html', context)

    # user = request.user
    #
    # if request.method == 'POST':
    #     true_password = user.password
    #
    #     old_password = request.POST.get('old_password')
    #     new_password1 = request.POST.get('new_password1')
    #     new_password2 = request.POST.get('new_password2')
    #
    #     #form = PasswordChangeForm(data=request.POST, user=request.user)
    #
    #     if true_password==old_password:
    #         if new_password1==new_password2:
    #             user.password=new_password2
    #             user.password.save()
    #             return redirect(reverse_lazy('home'))
    #         else:
    #             error_notice = "Hasła nie są identyczne. Spróbuj ponownie."
    #             return render(request, 'registration/password_change_form.html', {'error_notice': error_notice})
    #     else:
    #         error_notice = "Hasło nie pasuje. Spróbuj ponownie."
    #         return render(request, 'registration/password_change_form.html', {'error_notice': error_notice})
    # else:
    #     return render(request, 'registration/password_change_form.html', {'user': user})



