from django import forms
from django.contrib.auth.models import User
from django.core import validators

class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خود را وارد کنید', 'class': 'form-control'}),
        label='نام '
    )


    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را ولرد کنید'}),
        label='کلمه عبور'
    )



    def clean_user_name(self):
        user_name = self.cleaned_data.get('username')
        return user_name


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20,message='تعداد کاراکترهای وارد شده بیشتر از 20 نمیتواند باشد')

        ]
    )

    email = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator(message='ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را مجدد وارد کنید'}),
        label=' تکرار کلمه عبور '
    )


    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('کاربری با این نام کاربری ثبت نام کرده است')
        return user_name
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_id = User.objects.filter(email=email).exists()
        if is_exists_user_by_id:
            raise forms.ValidationError('کاربری با این ایمیل ثبت نام کرده است')
        return email


    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور باهم مغایرت دارند')
        return password

