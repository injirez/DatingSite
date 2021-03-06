from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from .models import Client
from .filters import UsersFilter
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm, NewUserFormInfo
from django.contrib.auth import login, authenticate

from .static.clients.pic_working import watermark_text
from .static.clients.utils.send_email import send_email
from django.contrib.gis.measure import D

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
                return redirect('https://datingsitetest.herokuapp.com/api/list/')
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
            return redirect('https://datingsitetest.herokuapp.com/api/clients/auth_info/')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='create.html', context={'register_form': form})

def auth_info(request):
    if request.method == 'POST':
        form = NewUserFormInfo(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            pic = request.FILES['photo']
            client.save()

            watermark_text(input_image_path='clients/static/clients/media/{}'.format(pic),
                           text='DatingSite',
                           pos=(0, 0))

            messages.success(request, 'Registration info successful.')
            return redirect('https://datingsitetest.herokuapp.com/api/list/')
        else:
            messages.error(request, 'Unsuccessful info registration. Invalid information.')
    form = NewUserFormInfo()

    return render(request=request, template_name='info.html', context={'form': form})


def match(request, user_id):
    if request.method == 'GET':
        data = Client.objects.get(pk=user_id)
        photo = data.photo.name[15:]
        context = {
            'username': data.user.username,
            'name': data.name,
            'surname': data.surname,
            'gender': data.gender,
            'email': data.email,
            'photo': photo,
        }
    return render(request=request, template_name='match.html', context=context)

def set_like(request, user_id):
    data = Client.objects.get(pk=user_id)

    user = Client.objects.get(pk=user_id)
    user_pk = user.user.pk

    viewer = Client.objects.get(user=User.objects.get(pk=request.user.pk))
    viewer.liked_users.add(user_pk)

    for liked_user in list(data.liked_users.all()):
        if str(request.user.username) == str(liked_user):
            print('{} and {} love each other'.format(request.user.username, data.user))

            send_email(receiver_email=str(data.email),
                       message='Subject: Dating site \n\n {} likes you! Email of user: {}'.format(str(request.user.username), viewer.email))
            send_email(receiver_email=str(viewer.email),
                       message='Subject: Dating site \n\n {} likes you! Email of user: {}'.format(str(data.user.username), data.email))

    try:
        Client.objects.get(pk=user_id+1)
        return HttpResponseRedirect('https://datingsitetest.herokuapp.com/api/clients/{}/match/'.format(user_id+1))
    except:
        return HttpResponse('Exception: Data Not Found')

    return HttpResponseRedirect('https://datingsitetest.herokuapp.com/api/list/')


def set_dislike(request, user_id):

    try:
        Client.objects.get(pk=user_id + 1)
        return HttpResponseRedirect('https://datingsitetest.herokuapp.com/api/clients/{}/match/'.format(user_id + 1))
    except:
        return HttpResponse('Exception: Data Not Found')

    return HttpResponseRedirect('https://datingsitetest.herokuapp.com/api/list/')

def users_list(request):
    if request.method == 'GET':
        users = UsersFilter(request.GET, queryset=Client.objects.all())


    return render(request=request, template_name='list.html', context={'filter': users})

def list_distance(request, distance):
    if request.method == 'GET':
        user_profile = Client.objects.first()
        items = []
        res = Client.objects.filter(location__distance_lte=(user_profile.location, D(km=distance)))
        for client in res:
            item = []
            item.append(client.user.username)
            item.append(client.name)
            item.append(client.surname)
            item.append(client.gender)
            item.append(client.email)
            item.append(client.photo.name)
            items.append(item)

        context = {
            'items': items,
        }
    return render(request=request, template_name='distance.html', context=context)

