from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_user')
def home(request):
    return render(request, 'index.html')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login_user')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Your username or password is incorrect! Please try again")

    return render(request, 'login.html', {})


def log_out(request):
    logout(request)
    return redirect('login_user')


def profile(request):
    return render(request, 'profile.html')