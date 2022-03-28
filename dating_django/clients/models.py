from django.db import models

class Client(models.Model):
    name = models.CharField('Name of client', max_length=20)
    surname = models.CharField('Surname of client', max_length=30)
    gender = models.CharField('Gender of client', max_length=1, choices=(('м', 'мужской'), ('ж', 'женский')))
    email = models.EmailField('Email of client', max_length=200)
    photo = models.ImageField('Image of client', upload_to='images/')
