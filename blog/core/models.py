from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import django_filters


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


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.EmailField(max_length=200, unique=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, upload_to='posts', default='Image')


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    title__gt = django_filters.CharFilter(field_name='title', lookup_expr='gt')
    title__lt = django_filters.CharFilter(field_name='title', lookup_expr='lt')

    created = django_filters.NumberFilter(field_name='created', lookup_expr='date')
    created__gt = django_filters.NumberFilter(field_name='created', lookup_expr='date__gt')
    created__lt = django_filters.NumberFilter(field_name='created', lookup_expr='date__lt')

    class Meta:
        model = Posts
        fields = ['title', 'content', 'created', 'status']