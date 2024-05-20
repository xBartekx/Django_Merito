# Django_Merito
Projekt z programowania zaawansowanego: Biblioteka On-line

Języki użyty w projekcie: Python, HTML, CSS
Framework, na ktorym oparto projekt: Django

Opis projektu: Jest to początkowy etap strony internetowej mogącej docelowo zyskać wiele nowych funkcjonalności w miarę rozwoju projektu. Wersja ta jest "demem" Biblioteki On-line, gdzie zalogowany użytkownik może wprowadzać książki do swojej kolekcji przeczytanych tytułów. Skupiono się na osiągnięciu celów podanych
w instrukcjach laboratoryjnych.


Poglądowy spis kroków wyrażonych w "commitach" wykonywanych podczas tworzenia projektu:

1. Początkowo zainstalowano i skonfigurowano interpreter Pyhon'a (wersji 3.12.3) oraz zainstalwoano framework Django (5.0.6)
2. Utworzono zdalne repozytorium na koncie github i połączono je z lokalnym aby móc puszczać commit'y z aktualizacjami projektu
3. Pierwsze commit'y dotyczyły przesłania utworzonego szkieletu katalogów projektu i aplikacji, które mają się w nim znajdować. 
   W fazie początkowej, kilka razy zrestartowano projekt i zaczęto pisanie skryptów od początku.
4. W jednym z kolejnych commitów udało się przesłać stabilny kod i uporządkowany zarys strony, na której ma funkcjonować biblioteka. Obejmował on: 
- utworzenie strony startowej i konfiguracja widoków domyślnych
- wygenerowanie i uruchomienie panelu administracyjnego oraz jego testy na serwerze deweloperskim
- utworzenie podstawowych modeli danych i kilku podstawowych klas pozwalających na dodawanie książek wraz z ich opisem oraz ogólną manipulację na danych
- ulepszenie panelu administracyjnego
5. Następny większy commit obejmował:
- konfigurację i wdrożenie aplikacji django-registration, służącej do zarządzania użytkownikami
- ulepszenie i poprawienie w html'u strony logowania, formularza rejestracji i widoku wylogowania a także zmodyfikowanie odpowiadających za nie funkcji
- ustawienie odpowiednich przekierowań URL
6. Dodano Commit z poprawkami dotyczącymi działania bazy danych i utworzono funkcję wyświetlającą listę książek