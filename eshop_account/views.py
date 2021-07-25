from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, EditUserForm
from django.contrib.auth import login,authenticate,get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request ,username=user_name ,password=password)
        

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            login_form.add_error('username','کاربری با مشخصات وارد شده یافت نشد')

        print(login_form.cleaned_data)
    context = {
        'login_form': login_form
    }
    return render(request,'account/login.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')


    context = {
        'register_form':register_form
    }

    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect("/login")

@login_required(login_url='/login')
def user_account_main_page(request):
    context = {}
    return render(request, 'account/user_account_main.html', context)

@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    edit_user_form = EditUserForm( request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
    
    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()
    
    context = {
        'edit_form': edit_user_form
    }
    return render(request, 'account/edit_account.html', context)

def user_sidebar(request):
    context = {}
    return render(request, 'account/user_sidebar.html', context)

