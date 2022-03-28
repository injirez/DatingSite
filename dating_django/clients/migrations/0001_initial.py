# Generated by Django 3.2.12 on 2022-03-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name of client')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname of client')),
                ('gender', models.CharField(choices=[('м', 'мужской'), ('ж', 'женский')], max_length=1, verbose_name='Gender of client')),
                ('email', models.EmailField(max_length=200, verbose_name='Email of client')),
                ('photo', models.ImageField(upload_to='', verbose_name='Image of client')),
            ],
        ),
    ]