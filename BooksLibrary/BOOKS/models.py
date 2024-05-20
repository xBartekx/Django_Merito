# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    verbose_name_plural = 'Książki'

class Books(models.Model):
    LARGE = 'T'
    MEDIUM = 'P'
    SMALL = 'M'
    OKŁADKA = (
        (LARGE, 'twarda'),
        (MEDIUM, 'personalizowana'),
        (SMALL, 'miękka'),
    )
    tytuł = models.CharField(verbose_name='Tytuł', max_length=50, default='Unknown Title')
    autor = models.CharField(verbose_name='Autor', max_length=50, default='Unknown Author')
    opis = models.TextField(blank=True, help_text='Opis Książki')
    okładka = models.CharField(max_length=1, choices=OKŁADKA, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField('Data wydania')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __unicode__(self):
        return u'%s' % (self.nazwa)


class Genre(models.Model):
    książka = models.ForeignKey(Books,
                              on_delete=models.CASCADE,
                              related_name='Gatunek')
    nazwa = models.CharField(verbose_name=u"Gatunek", max_length=30)
    jarski = models.BooleanField(
        default=False,
        verbose_name=u"Tagi",
        help_text=u"Zaznacz, jeżeli treść jest nie odpowiednia dla"
        u" Osoby wrażliwe")

    def __unicode__(self):
        return u'%s' % (self.nazwa)

