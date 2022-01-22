from django.db import models
from django.core import validators


class MyDb(models.Model):
    email = models.EmailField(max_length=30, verbose_name="Email",
                              validators=[validators.EmailValidator],
                              error_messages={'invalid': 'Email вказано некоректно'})

    class Meta:
        verbose_name_plural = "Emails"
        verbose_name = "Email"
        ordering = ["email"]
