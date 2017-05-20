from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)


		