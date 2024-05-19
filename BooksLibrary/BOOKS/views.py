from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render(request, 'BOOKS/index.html')

# def index(request):
#     """Strona główna"""
#     kontekst = {'komunikat': 'Witaj w aplikacji Biblioteka On-Line!'}
#     return render(request, 'BOOKS/index.html', kontekst)

# def logout(request):
#     """Strona wylogowania"""
#     kontekst = {'komunikat': 'Wylogowano z aplikacji Biblioteka On-Line!'}
#     return render(request, 'registration/logout.html', kontekst)


def logout_view(request):
    logout(request)
    return redirect('BOOKS/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatyczne logowanie nowo zarejestrowanego użytkownika
            messages.success(request, 'Rejestracja zakończona sukcesem.')
            return redirect('BOOKS/index.html')  # przekierowanie po rejestracji
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Zalogowano jako {username}.")
                return redirect('BOOKS') 
            else:
                messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło.")
        else:
            messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})