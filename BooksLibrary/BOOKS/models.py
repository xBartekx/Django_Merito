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
    BLANK = ''
    DRAMAT = 'Dramat'
    KOMEDIA = 'Komedia'
    HORROR = 'Horror'
    ROMANTYCZNA = 'Romatyczna'
    EDUKACYJNA = 'Edukacyjna'
    HISTORYCZNA = 'Historyczna'
    KRYMINAŁ = 'Kryminał'
    GATUNEK = (
        (BLANK, ''),
        (DRAMAT, 'Dramat'),
        (KOMEDIA, 'Komedia'),
        (HORROR, 'Horror'),
        (ROMANTYCZNA, 'Romantyczna'),
        (EDUKACYJNA, 'Edukacyjna'),
        (HISTORYCZNA, 'Historyczna'),
        (KRYMINAŁ, 'Kryminał'),
    )


    tytuł = models.CharField(verbose_name='Tytuł', max_length=50, default='Unknown Title')
    gatunek = models.CharField(max_length=40, choices=GATUNEK, default='Unknown Genre')
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

class Review(models.Model):
    książka = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='recenzje')
    użytkownik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recenzje')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tytuł = models.CharField(max_length=100, verbose_name='Tytuł Recenzji')
    treść = models.TextField(verbose_name='Treść Recenzji')
    ocena = models.PositiveSmallIntegerField(verbose_name='Ocena', choices=[(i, str(i)) for i in range(1, 6)])
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Recenzje'

    def __str__(self):
        return f"{self.tytuł} - {self.użytkownik}"

