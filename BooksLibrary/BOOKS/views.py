from django.shortcuts import render

def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Biblioteka On-Line!'}
    return render(request, 'BOOKS/index.html', kontekst)
