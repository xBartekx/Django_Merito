# Generated by Django 5.0.6 on 2024-05-18 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50, verbose_name='Książka')),
                ('opis', models.TextField(blank=True, help_text='Opis Książki')),
                ('okładka', models.CharField(choices=[('T', 'twarda'), ('P', 'personalizowana'), ('M', 'miękka')], default='T', max_length=1)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data wydania')),
            ],
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='Gatunek')),
                ('jarski', models.BooleanField(default=False, help_text='Zaznacz, jeżeli treść jest nie odpowiednia dla Osoby wrażliwe', verbose_name='jarski?')),
                ('książka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gatunek', to='BOOKS.books')),
            ],
        ),
    ]
