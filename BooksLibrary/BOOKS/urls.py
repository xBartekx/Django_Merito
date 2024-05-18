from django.urls import path
from BOOKS import views  # import widoków aplikacji

app_name = 'BOOKS'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='BOOKS_index'),
]