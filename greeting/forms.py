from django.forms import ModelForm
from django import forms
from django.core import validators
from greeting.models import MyDb


class MyDbForm(ModelForm):
    """The form for receiving an email from user"""
    email = forms.EmailField(label='Вкажіть Ваш email:',
                             validators=[validators.EmailValidator],
                             error_messages={'invalid': 'Email введено некоректно'})

    class Meta:
        model = MyDb
        fields = ('email',)
