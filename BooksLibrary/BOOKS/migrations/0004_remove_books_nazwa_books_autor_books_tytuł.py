# Generated by Django 5.0.6 on 2024-05-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKS', '0003_alter_genre_jarski'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='nazwa',
        ),
        migrations.AddField(
            model_name='books',
            name='autor',
            field=models.CharField(default='Unknown Author', max_length=50, verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='books',
            name='tytuł',
            field=models.CharField(default='Unknown Title', max_length=50, verbose_name='Tytuł'),
        ),
    ]
