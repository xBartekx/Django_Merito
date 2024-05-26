from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Books, Review
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ReviewForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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

def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_list(request):
    books = Books.objects.filter(user=request.user)
    return render(request, 'BOOKS/book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return redirect('BOOKS:book_list')
        except ValidationError as e:
            form.add_error(None, str(e))
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def update_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        try:
            if form.is_valid():
                form.save()
                return redirect('BOOKS:book_list')
        except ValidationError as e:
            form.add_error(None, str(e))
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        try:
            book.delete()
            return redirect('BOOKS:book_list')
        except Exception as e:
            return render(request, 'books/book_list.html', {'error': str(e)})
    return render(request, 'books/delete_book.html', {'book': book})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    reviews = Review.objects.filter(książka=book)
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'books/book_detail.html', context)

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.książka = book
            review.użytkownik = request.user
            review.autor = request.user
            review.save()
            return redirect('BOOKS:book_detail', book_id=book_id)
    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form': form, 'book': book})