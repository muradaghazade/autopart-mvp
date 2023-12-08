from django.urls import path
from core.views import *
from accounts.views import UserProfileView, ShopProfileView , LoginUserView ,RegisterView ,ShopRegisterView, UDetailView ,PDetailView,ForgetPasswordView, ResetPasswordView, UpdatePasswordView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
     path('profile/<slug:slug>/',UserProfileView.as_view(),name ='profile'),
     path('shop/<slug:slug>/',ShopProfileView.as_view(),name ='shop'),
     path('login/',LoginUserView.as_view(),name ='login'),
     path('register/',RegisterView.as_view(),name ='register'), 
     path('shopreg/',ShopRegisterView.as_view(),name ='shopregister'), 
     path('log-out', LogoutView.as_view(), name='log-out'),
     path('udetail/<slug:slug>/',UDetailView.as_view(),name ='detail'),
     path('pdetail/<slug:slug>/',PDetailView.as_view(),name ='pdetail'),

     path('change-password/', UpdatePasswordView.as_view(), name='change-password'),
     path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),
     path('password-reset-confirm/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name = 'password-reset-confirm'),


     
]