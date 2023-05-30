import sqlite3
import ssl
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score

ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url, header=None)

column_names = ["Type", "Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
                "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
                "OD280_OD315_of_diluted_wines", "Proline"]

df.columns = column_names

zmienna_objasniana = "Type"


#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)
print("zad1")
wynik1 = list(df.columns)
print(wynik1)

#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
print("zad2")
wynik2 = f"Liczba wierszy: {df.shape[0]}, Liczba kolumn: {df.shape[1]}"
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.

class Wine:
    def __init__(self, variables, target):
        self.variables = variables
        self.target = target

    def __repr__(self):
        return f"Wine(variables={self.variables}, target={self.target})"

    def create_new(self):
        return Wine(self.variables.copy(), self.target)

#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
print("zad3")
wynik3 = Wine(variables=["Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
                         "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
                         "OD280_OD315_of_diluted_wines", "Proline"],
              target="Type") #do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
##Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
print("zad4")

wineList = []
for index, row in df.iterrows():
    wine = Wine(variables=row[:-1].tolist(), target=row[-1])
    wineList.append(wine)

wynik4 = len(wineList)
print(wynik4)


#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
print("zad5")

last_wine = wineList[-1]
new_wine = eval(repr(last_wine))
wynik5 = last_wine
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:

print("zad6")

conn = sqlite3.connect('wines_Kacper_Gajowniczek.db')
df.to_sql('wines', conn, if_exists='replace', index=False)

# Wczytanie danych z tabeli wines, wybierając tylko wiersze z typem wina nr 3
query = "SELECT * FROM wines WHERE Type = 3"
df_filtered = pd.read_sql_query(query, conn)

conn.close()

wynik6 = df_filtered

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:
print("zad7")

model = LogisticRegression()


wynik7 = model.__class__.__name__

print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)
print("zad8")

X = df.drop(columns=['Type'])
y = df['Type']

# Normalizacja danych objaśniających
X = preprocessing.normalize(X)

model = LogisticRegression()

# Wytrenowanie modelu na wszystkich danych
model.fit(X, y)

# Sprawdzian krzyżowy z użyciem LeaveOneOut
loo = LeaveOneOut()
y_true = []
y_pred = []

for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y.iloc[test_index]

    model.fit(X_train, y_train)
    y_true.append(y_test.iloc[0])
    y_pred.append(model.predict(X_test)[0])

wynik8 = accuracy_score(y_true, y_pred)

print(wynik8)