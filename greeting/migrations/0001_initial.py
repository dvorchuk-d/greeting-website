# Generated by Django 4.0.1 on 2022-01-22 12:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(error_messages={'invalid': 'Email вказано некоректно'}, max_length=30, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'ordering': ['email'],
            },
        ),
    ]
