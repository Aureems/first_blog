from django.urls import path
from .views import home, register, login_user, log_out, profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name="register"),
    path('login/', login_user, name="login_user"),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile')
]