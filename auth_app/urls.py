from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, logout_user

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')

]