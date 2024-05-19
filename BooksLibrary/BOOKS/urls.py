from django.urls import path
from BOOKS import views  # import widoków aplikacji
from django.contrib.auth import views as auth_views
from . import views

app_name = 'BOOKS'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('konta/login/', auth_views.LoginView.as_view(), name='login'),
    path('konta/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('konta/register/', views.register, name='register'),
]


