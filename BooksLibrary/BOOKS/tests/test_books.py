import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from BOOKS.models import Books
from django.utils import timezone
from decimal import Decimal
from django.test import Client
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

# Poniżej 10 testów za pomocą modułu "pytest":

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def book(user):
    return Books.objects.create(
        tytuł='Test Book',
        autor='Test Author',
        opis='Test Description',
        okładka='T',
        cena=Decimal('19.99'),
        data=timezone.now().date(),
        user=user
    )


@pytest.mark.django_db
def test_add_book(client, user):
    client.login(username='testuser', password='testpass')
    url = reverse('BOOKS:add_book')
    data = {
        'tytuł': 'New Book',
        'autor': 'New Author',
        'opis': 'New Description',
        'okładka': 'M',
        'cena': '29.99',
        'data': '2024-05-01',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Books.objects.count() == 1
    book = Books.objects.first()
    assert book.tytuł == 'New Book'


@pytest.mark.django_db
def test_delete_book(client, user, book):
    client.login(username='testuser', password='testpass')
    url = reverse('BOOKS:delete_book', args=[book.id])
    response = client.post(url)
    assert response.status_code == 302
    assert Books.objects.count() == 0


@pytest.mark.django_db
def test_list_books(client, user, book):
    client.login(username='testuser', password='testpass')
    url = reverse('BOOKS:book_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Test Book' in response.content.decode()


@pytest.mark.django_db
def test_search_books(client, user, book):
    client.login(username='testuser', password='testpass')
    url = reverse('BOOKS:book_list')
    response = client.get(url + '?q=Test')
    assert response.status_code == 200
    assert 'Test Book' in response.content.decode()


@pytest.fixture
def client_logged_in(client, user):
    client.login(username='testuser', password='testpass')
    return client


@pytest.mark.django_db
def test_logout_view(client_logged_in):
    response = client_logged_in.get(reverse('logout'))
    assert response.status_code == 405


@pytest.mark.django_db
def test_update_book(client_logged_in, book):
    url = reverse('BOOKS:update_book', args=[book.id])
    data = {
        'tytuł': 'Updated Book',
        'autor': 'Updated Author',
        'opis': 'Updated Description',
        'okładka': 'M',
        'cena': '24.99',
        'data': '2024-05-15',
    }
    response = client_logged_in.post(url, data)
    assert response.status_code == 302
    updated_book = Books.objects.get(pk=book.id)
    assert updated_book.tytuł == 'Updated Book'


@pytest.mark.django_db
def test_delete_book_invalid_user(client_logged_in, user):
    another_user = User.objects.create_user(username='anotheruser', password='testpass')
    book = Books.objects.create(
        tytuł='Test Book',
        autor='Test Author',
        opis='Test Description',
        okładka='T',
        cena=Decimal('19.99'),
        data=timezone.now().date(),
        user=another_user
    )
    url = reverse('BOOKS:delete_book', args=[book.id])
    response = client_logged_in.post(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_book_unauthenticated(client):
    url = reverse('BOOKS:add_book')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_book_list_unauthenticated(client):
    url = reverse('BOOKS:book_list')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_book_list_authenticated(client_logged_in, book):
    url = reverse('BOOKS:book_list')
    response = client_logged_in.get(url)
    assert response.status_code == 200
    assert 'Test Book' in response.content.decode()


import pytest
from .models import Review, Books, User


@pytest.mark.django_db
def test_create_review():
    user = User.objects.create(username='testuser')
    book = Books.objects.create(title='Test Book', author='Test Author')

    review = Review.objects.create(
        książka=book,
        użytkownik=user,
        tytuł='Test Review',
        treść='Lorem ipsum dolor sit amet.',
        ocena=5
    )

    saved_reviews = Review.objects.all()
    assert len(saved_reviews) == 1
    assert saved_reviews[0].tytuł == 'Test Review'
    assert saved_reviews[0].książka == book
    assert saved_reviews[0].użytkownik == user


@pytest.mark.django_db
def test_foreign_key_relationship():
    user = User.objects.create(username='testuser')
    book = Books.objects.create(title='Test Book', author='Test Author')

    review = Review.objects.create(
        książka=book,
        użytkownik=user,
        tytuł='Test Review',
        treść='Lorem ipsum dolor sit amet.',
        ocena=5
    )

    assert review.książka == book
    assert review.użytkownik == user


@pytest.mark.django_db
@pytest.mark.parametrize('ocena', [1, 2, 3, 4, 5])
def test_create_review_with_different_ratings(ocena):
    user = User.objects.create(username='testuser')
    book = Books.objects.create(title='Test Book', author='Test Author')

    review = Review.objects.create(
        książka=book,
        użytkownik=user,
        tytuł=f'Test Review {ocena}',
        treść='Lorem ipsum dolor sit amet.',
        ocena=ocena
    )

    saved_reviews = Review.objects.filter(ocena=ocena)
    assert len(saved_reviews) == 1
    assert saved_reviews[0].tytuł == f'Test Review {ocena}'
    assert saved_reviews[0].książka == book
    assert saved_reviews[0].użytkownik == user
    assert saved_reviews[0].ocena == ocena



