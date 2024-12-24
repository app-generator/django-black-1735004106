# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Book(models.Model):

    #__Book_FIELDS__
    nombre = models.TextField(max_length=255, null=True, blank=True)
    hojas = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    tomo = models.IntegerField(null=True, blank=True)
    publicado = models.DateTimeField(blank=True, null=True, default=timezone.now)
    autor = models.ForeignKey(Creador, on_delete=models.CASCADE)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")


class Creador(models.Model):

    #__Creador_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Creador_FIELDS__END

    class Meta:
        verbose_name        = _("Creador")
        verbose_name_plural = _("Creador")



#__MODELS__END
