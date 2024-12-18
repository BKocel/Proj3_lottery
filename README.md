## Nazwa programu: "Loteria" <br> Plik zawierający program: "main.py"

#### Opis działania programu:
Program wybraną przez użytkownika liczbę losowych cyfr <br>

#### Użyte zmienne i ich typy:
1. **lenght** - typ *int*, przechowuje wybraną przez użytkownika ilość wygenerowanych cyfr; <br>
2. **rand** - typ *int*, przechowuje aktualnie wygenerowaną cyfrę; <br>
3. **lotto_numbers** - typ *list*, przechowuje wszystkie wygenerowane cyfry.<br>

#### Najważniejsze funkcje:
1. Funkcja ***random.randrange(a, b)*** z biblioteki **random**, użyta do generowania losowych wartości zmiennoprzecinkowych z zakresu a - b (konwertowanych potem do liczby całkowitej); <br>
2. Funkcja ***time.sleep*** z biblioteki **time**, użyta aby budować napięcie, przed podaniem numerów; <br>

#### Działanie programu:
Program pyta użytkownika o ilość numerów. Poczym podaje wybraną ilość liczb pseudolosowych.

Przykładowo:
```
Witamy w generatorze liczb lotto!
Ile cyfr chcesz wylosować? 12
Proszę czekać, generowanie numerów
2 8 4 9 1 7 9 7 1 8 4 5
```
