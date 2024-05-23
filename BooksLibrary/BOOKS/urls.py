from django.urls import path
from BOOKS import views  # import widoków aplikacji
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Books

app_name = 'BOOKS'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('konta/login/', auth_views.LoginView.as_view(), name='login'),
    path('konta/logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('konta/register/', views.register, name='register'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]


