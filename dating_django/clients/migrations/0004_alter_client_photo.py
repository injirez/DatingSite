# Generated by Django 3.2.12 on 2022-03-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='clients/static/clients/media', verbose_name='Image of client'),
        ),
    ]
