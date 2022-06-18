from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, EmployeeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Employee, User

# Create your views here.


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    login_url = 'login_user'
    form_class = EmployeeForm
    template_name = 'create.html'
    success_url = '/'


class EmployeeListView(ListView):
    model = Employee
    login_url = 'login_user'
    template_name = 'index.html'
    success_url = '/'
    paginate_by = 2


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    login_url = 'login_user'
    form_class = EmployeeForm
    template_name = 'update.html'
    success_url = '/'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    login_url = 'login_user'
    template_name = 'delete.html'
    success_url = '/'


class UserEditView(UpdateView):
    model = User
    login_url = 'login_user'
    template_name = 'edituser.html'
    success_url = '/'
    fields = ['fullname', 'email', 'phone', 'mobile', 'address', 'job', 'photo']


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

    return render(request, 'index.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def user_profile(request):
    return render(request, 'profile.html')


def edit_user(request):
    return render(request, 'edituser.html')



