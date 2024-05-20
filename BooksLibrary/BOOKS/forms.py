from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['tytuł', 'autor', 'data', 'cena', 'opis']