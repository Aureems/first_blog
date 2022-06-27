from django.urls import path
from .views import register, login_user, logout_user, user_profile, EmployeeCreateView, EmployeeListView, EmployeeUpdateView, EmployeeDeleteView, UserEditView, PostsList, PostsDetail, PostsEdit, PostsCreate, PostsDelete

urlpatterns = [
    path('', EmployeeListView.as_view(), name='home'),
    path('register/', register, name="register"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', user_profile, name='profile'),
    path('create/', EmployeeCreateView.as_view(), name='create'),
    path('update/<pk>', EmployeeUpdateView.as_view(), name='update'),
    path('delete/<pk>', EmployeeDeleteView.as_view(), name='update'),
    path('edituser/<pk>', UserEditView.as_view(), name='edit_user'),
    path('posts/', PostsList.as_view(), name='posts'),
    path('posts_detail/<slug:slug>/', PostsDetail.as_view(), name='posts_detail'),
    path('posts_edit/<slug:slug>', PostsEdit.as_view(), name='posts_edit'),
    path('posts_create/', PostsCreate.as_view(), name='posts_create'),
    path('posts_delete/<slug:slug>', PostsDelete.as_view(), name='posts_delete'),
]