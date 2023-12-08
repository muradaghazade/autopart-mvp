from django import forms 
from accounts.models import User

from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm , UsernameField, PasswordResetForm , UserCreationForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : '****',
                'class' : 'email-input',
            }))
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifreni tekrarla',
                'class' : 'email-input',
            }))

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'email-input',
            })
        )
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'adınızı daxil edin', 'class': 'email-input'}),
            }



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'email-input',
        'placeholder': 'Username',
        'name': 'username'
    }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'email-input',
            'name': 'password',
            'placeholder': 'Password'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password']







class  ShopRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : '****',
                'class' : 'email-input',
            }))
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifreni tekrarla',
                'class' : 'email-input',

            }))

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'email-input',
            })
        )


    # image = forms.FileField(),'image'

    
    class Meta:
        model = User
        fields = ('full_name','email','password1','password2','number','adress','description','username')
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'Ad', 'class': 'email-input'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Ad', 'class': 'email-input'}),
            'number': forms.TextInput(attrs={'id': 'number', 'placeholder': 'Əlaqə', 'class': 'email-input'}),

            'adress': forms.TextInput(attrs={'id': 'adress', 'placeholder': 'Ünvan', 'class': 'email-input'}),
            
            'description': forms.TextInput(attrs={'id': 'description', 'placeholder': '', 'class': 'email-input'}),
            # 'Avtomobil_markası': forms.ChoiceField(attrs={choices==CHOICES}),


            }

class ThePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifrə ',
                'class' : 'password-input',
            }))

    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Yeni şifrə ',
                'class' : 'password-input',
            }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifrəni təsdiqlə',
                'class' : 'password-input',
            }))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'email-input',
        })
    )

class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'password-input',
             }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password again',
                'class' : 'password-input',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )