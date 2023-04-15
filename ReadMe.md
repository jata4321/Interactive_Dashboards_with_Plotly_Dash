# Schemat podejścia do budowy nowego Dashboard.

## Krok 1. Poznaj bazę danych, z której pobierzesz informacje.
Otwórz plik na przykład `csv` lub `db3` i zastanów się których kolumn będziesz używał.
Można posłużyć się `Jupyter Notebook` w celu poznania struktury danych.

## Krok 2. Stwórz niezbędne pliki do pracy.
W edytorze np. **PyCharm** stwórz nowy katalog, następnie plik i wczytaj do niego niezbędne 
biblioteki, które wykorzystasz w budowie dashboard. Będziesz je używał do
ładowania danych, budowy z core components, html componens, funkcji `callback`.
(Pamiętaj o strukturze katalogów danych i o tym, że sięganie do nich w różnych
systemach operacyjnych odbywa się w inny sposób).
```python
from dash import Dash, dcc, html, dash_table
```


Następnie utwórz obiekt `app`.
```python
app = Dash()
```

## Krok 3. Zbuduj layout.
Użyj komendy layout do obiektu app, żeby stworzyć szkielet strony aplikacji.
Wstaw do niego **html.Div** zawierający trzy komponenty:
```python
app.layout = html.Div([
    html.H1(),
    dcc.Dropdown(),
    dcc.Graph()
])
``` 
Użyj `plotly.express()` do generowania wykresu.

## Krok 4. Dodaj dekorator i funkcję callback.
Napisz sekcję dekoratora i funkcji callback, rozpoczynając od `@app.callback()`
Wypisz wszystkie `Outputs`, `Inputs`, `States`. Pamiętaj o kolejności oraz porządku
przekazywania zmiennych do funkcji.

Struktura powinna mieć wygląd:

```python
@app.callback(
    Output(id, własność),
    Input(id, własność),
    State(id, własność)
)
def funkcja_zwracająca_obiekty(zmienna1,zmienna2)
    return obiekt
```
Obiektem mogą być różne rzeczy: `children`, `value` lub `figure`.

## Krok 5. Uruchom aplikację dashboard.
Dodaj kod uruchamiający server z opcją debug ustawioną na `True`. Posłuż się
do tego poniższym kodem:
```python
if '__name__' == '__main__':
    app.run(debug=True)
```