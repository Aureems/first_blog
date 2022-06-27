from django.contrib import admin
from .models import Employee, User, Posts
from django_admin_filter.filters import CustomFilter


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'phone', 'email']
    list_filter = ['name', 'department', 'phone', 'email']


admin.site.register(Employee, EmployeeAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'fullname', 'phone', 'mobile', 'address', 'photo']


admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Posts, PostAdmin)