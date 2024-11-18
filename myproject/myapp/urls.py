from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Trang chủ
    path('', views.index, name='index'),

    # Đăng nhập và đăng xuất
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # Đăng ký
    path('register/', views.register, name='register'),

    # Tạo bài viết
    path('create/', views.create_post, name='create_post'),
]
