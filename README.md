# Django_Merito
Projekt z programowania zaawansowanego: Biblioteka On-line

Języki użyty w projekcie: Python, HTML, CSS
Framework, na ktorym oparto projekt: Django

Opis projektu: Jest to początkowy i ogólny zarys strony internetowej mogącej docelowo zyskać wiele nowych funkcjonalności w miarę rozwoju projektu. Wersja ta jest "demem" Biblioteki On-line a konkretnie jednym z jej modułów, który służy do tego aby zalogowany użytkownik mógł wprowadzać książki do swojej prywatnej kolekcji przeczytanych tytułów. Skupiono się na osiągnięciu wymagań podanych w instrukcjach laboratoryjnych. Poniżej spis zrealizowanych celów:

a) Interfejs zawiera funkcjonalności: 
- Dodawanie zasobów 
- Usuwanie zasobów 
- Aktualizacja zasobów 
- Dodawanie Recenzji
- Wyświetlanie Recenzji
- Wyświetlanie informacji o istniejących zasobach
- komunikacja z użytkownikiem i wprowadzania danych z klawiatury wraz z ich weryfikacją
- szereg możliwość i restrykcji odnośnie wprowadzania różnych typów danych
- obsługa błędów (try: ...except...) wraz z wyświetlanym komunikatem
b) Strona posiada zaimplementowany i w pełni funkcjonalny system administracyjny oraz funkcje rejestracji lub logowania użytkownika
c) Projekt wykorzystuje odpowiednio skonfigurowaną i przystosowaną bazę danych db.sqlite3, która umożliwia:
- Dodawanie obiektu do bazy 
- Usuwanie obiektu z bazy 
- Aktualizacja obiektu w bazie 
- Dodawanie recenzji do bazy
- Pobieranie wszystkich obiektów z bazy i wyświetlanie w formie listy dla użytkownika 
- Tabele mają określone (i dodatkowo opisane w skrypcie) typy danych, które są przechowywany w ich poszczególnych kolumnach
d) Testy:
- 




Historia najważniejszych "commitów" wykonywanych podczas tworzenia projektu:

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
6. Dodano commit z poprawkami dotyczącymi działania bazy danych i utworzono funkcję wyświetlającą listę książek
7. Przesłanie drobnych poprawek i ulepszeń dotyczących szroko pojętego wyglądu poszczególnych stron i formularzy
8. Commit z ostatecznymi poprawkami oraz dodatkowymi funkcjami. Ponadto zoptymalizowano i powiązano ze sobą poszczególne skrypty oraz szblony aby 
całość pozwalała na płynne wykorzystanie wszystkich zaimplementowanych mechanik i funkcjonalności pozwalając użytkowikom na stabilne i regularne korzystanie z jego własnej listy zapisanych książek w Bibioltece On-line.  
9. Commit dodający klasę Review zajmującą się recenzjami książek, użytkownik może dodawać oraz wyświetleć recenzje, które widzą inni użytkownicy. Recenzje składają się z: Tytułu recenzji, Treści recenzji oraz Oceny. Dodano testy do klasy review oraz test parametryczny testujący dodawanie ocen od 1 do 5.
