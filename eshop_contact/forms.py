from django import forms
from django.core import validators

class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام و نام خانوادگی خود را وارد کنید','class':"form-control"}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150,'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کارکتر باشد')]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'palceholder':'ایمیل ',
        'class':"form-control"}),
        label='ایمیل',
        validators= [
            validators.MaxLengthValidator(100,'ایمیل شما نمیتواند بیشتر از 100 کاراکتر شود')]

    )

    
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا موضوع پیام خود را وارد کنید', 'class':"form-control"}),
        label='موضوع پیام',
        validators=[
            validators.MaxLengthValidator(200,'موضوع پیام شما نمیتواند بیشتر از 200 کارکتر باشد')]
    )

    
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'لطفا متن خود را وارد کنید', 'class':"form-control"}),
        label='متن پیام'
    )
