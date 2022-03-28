from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .models import Client

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm, NewUserFormInfo
from django.contrib.auth import login, authenticate

def index(request):
    res = []
    for data in list(Client.objects.all()):
        res.append({'name': data.name, 'surname': data.surname, 'gender': data.gender, 'email': data.email, 'photo': data.photo.path})
    print(res)
    return HttpResponse(res)

def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('https://www.speedtest.net/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={'login_form': form})

def create(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('http://127.0.0.1:8000/api/clients/auth_info/')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='create.html', context={'register_form': form})

def auth_info(request):
    if request.method == 'POST':
        form = NewUserFormInfo(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            messages.success(request, 'Registration info successful.')
            return redirect('https://www.speedtest.net/')
        else:
            messages.error(request, 'Unsuccessful info registration. Invalid information.')
    form = NewUserFormInfo()

    return render(request=request, template_name='info.html', context={'form': form})
