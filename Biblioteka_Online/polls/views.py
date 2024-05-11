from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, genre=genre, published_date=published_date)
        return redirect('book_list')
    return render(request, 'add_book.html')

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('book_list')

