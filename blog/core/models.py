from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

LABELS = (
    ('NEW', 'New'),
    ('SECOND', 'Second'),
    ('THIRD', 'Third')
)


class Employee(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    label = models.CharField(max_length=6, choices=LABELS, default='NEW')

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=150)
    fullname = models.CharField(max_length=100, default='First Name, Last Name')
    email = models.CharField(verbose_name='email address', max_length=30, unique=True)
    phone = models.CharField(max_length=11, default='(xxx)xxxxxx',)
    mobile = models.CharField(max_length=11, default='+370xxxxxxx')
    job = models.CharField(max_length=50, default='Your current job')
    website = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='users', default='users/default.jpg')
    address = models.CharField(max_length=100, default='Street, City')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address', 'phone']

