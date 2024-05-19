from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Biblioteka On-Line!'}
    return render(request, 'BOOKS/index.html', kontekst)


# def logout(request):
#     """Strona wylogowania"""
#     kontekst = {'komunikat': 'Wylogowano z aplikacji Biblioteka On-Line!'}
#     return render(request, 'registration/logout.html', kontekst)


def logout_view(request):
    logout(request)
    return redirect('BOOKS')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatyczne logowanie nowo zarejestrowanego użytkownika
            return redirect('BOOKS')  # przekierowanie po rejestracji
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})