from django import forms
from .models import Books
import datetime
from django.core.exceptions import ValidationError
from decimal import Decimal 

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['tytuł', 'autor', 'data', 'cena', 'opis']


    def clean(self):
        cleaned_data = super().clean()
        tytuł = cleaned_data.get("tytuł")
        autor = cleaned_data.get("autor")
        data = cleaned_data.get("data")
        cena = cleaned_data.get("cena")

        if not isinstance(tytuł, str):
            self.add_error('tytuł', 'Tytuł musi być tekstem')
        if not isinstance(autor, str):
            self.add_error('autor', 'Autor musi być tekstem')
        if not isinstance(data, datetime.date):
            self.add_error('data', 'Data musi być poprawnym formatem daty')
        return cleaned_data

    def clean_data(self):
        data = self.cleaned_data.get("data")
        if data and data > datetime.date.today():
            raise ValidationError("Data publikacji nie może być w przyszłości.")
        return data

    def clean_cena(self):
        cena = self.cleaned_data.get("cena")
        if not isinstance(cena, (int, float, Decimal)):
            raise ValidationError("Cena musi być liczbą.")
        return cena