from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Name of client', max_length=20)
    surname = models.CharField('Surname of client', max_length=30)
    gender = models.CharField('Gender of client', max_length=1, choices=(('м', 'мужской'), ('ж', 'женский')))
    email = models.EmailField('Email of client', max_length=200)
    photo = models.ImageField('Image of client', upload_to='images/')
