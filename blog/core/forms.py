from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, User, Posts, STATUS



class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=False)
    email = forms.CharField(help_text=False)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'department', 'phone', 'email', 'address']


class EditUserForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11)
    mobile = forms.CharField(max_length=11)
    job = forms.CharField(max_length=50)
    website = forms.CharField(max_length=100)
    photo = forms.ImageField(max_length=100)
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone', 'mobile', 'address', 'job', 'photo']


class PostsEditForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=200)
    content = forms.CharField(max_length=10000)
    status = forms.ChoiceField(choices=STATUS)
    image = forms.ImageField(max_length=100)

    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'status', 'image']