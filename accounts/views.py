from django.shortcuts import render, redirect
from accounts.models import User 
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password
from django.views.generic import  DetailView , CreateView   
from accounts.forms import RegisterForm, LoginForm 
from django.contrib.auth.views import LoginView , PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from accounts.forms import ThePasswordChangeForm ,  ShopRegisterForm , ResetPasswordConfirmForm, ResetPasswordForm

class UserProfileView(DetailView):
    model = User
    template_name = "user-profile.html"
    context_object_name = "users"

class ShopProfileView(DetailView):
    model = User
    template_name = 'shop-profile.html'

    
class RegisterView(CreateView):
    model = User
    template_name = "user-register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

class ShopRegisterView(CreateView):
    model = User
    template_name = "shop-register.html"
    form_class = ShopRegisterForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class LoginUserView(LoginView):
    template_name = "log-in.html"
    form_class = LoginForm


class UDetailView(DetailView):
    model = User
    template_name = 'user-detail.html'

class PDetailView(DetailView):
    model = User
    template_name = 'product-detail.html'

class UpdatePasswordView(PasswordChangeView):
    template_name = 'change-password.html'
    form_class = ThePasswordChangeForm
    success_url = reverse_lazy('accounts:login')


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'forgotPsw.html'
    success_url = reverse_lazy('accounts:change-password')
    email_template_name = 'password_reset_email.html'


class ResetPasswordView(PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name= "password_reset_confirm.html" 
    success_url = reverse_lazy('accounts:login')


 