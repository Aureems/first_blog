from django.contrib import admin
from .models import Employee, User


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'phone', 'email']
    list_filter = ['name', 'department', 'phone', 'email']


admin.site.register(Employee, EmployeeAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'fullname', 'phone', 'mobile', 'address', 'photo']


admin.site.register(User, UserAdmin)
