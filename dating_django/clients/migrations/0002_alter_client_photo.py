# Generated by Django 3.2.12 on 2022-03-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='images/', verbose_name='Image of client'),
        ),
    ]
