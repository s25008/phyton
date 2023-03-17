#Kalkulator
print("Podaj jaka operacje chcesz wykonac ?")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Modulo")
print("6. Potegowanie")
zadanie = input("zadanie:")
dana1 = input("Podaj pierwsza dana")
dana2 = input("Podaj druga dana")
if zadanie == "1":
    print(int(dana1) + int(dana2))

if zadanie == "2":
    print(int(dana1) - int(dana2))

if zadanie == "3":
   print(int(dana1) * int(dana2))

if zadanie == "4":
    print(int(dana1) / int(dana2))

if zadanie == "5":
    print(int(dana1) % int(dana2))

if zadanie == "6":
    print(int(dana1) ** int(dana2))

#Ankieta
print("Podaj Imie i Nazwisko")
imie = input("Podaj swoje Imie")
nazwisko = input("Podaj Nazwisko")
pytanie1 = "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:"
print(pytanie1)
odp11 = "1:oglądanie telefizji/filmów/seriali"
odp12 = "2:czytanie książek/czasopism"
odp13 = "3:słuchanie muzyki"
print(odp11)
print(odp12)
print(odp13)
odpu1 = input("Odpowiedź:")

pytanie2 = "W jakich okolicznościach czytasz książki najczęściej?:"
print(pytanie2)
odp21 = "1:podczas podróży"
odp22 = "2:w czasie wolnym (po pracy, na urlopie)"
odp23 = "3:w ogóle nie czytam"
print(odp21)
print(odp22)
print(odp23)
odpu2 = input("Odpowiedź:")

pytanie3 = "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?:"
print(pytanie3)
odp31 = "1:chęć poszerzenia wiedzy"
odp32 = "2:czytanie to moje hobby"
odp33 = "3:odczuwam presję rodziny/środowiska, żeby czytać"
print(odp31)
print(odp32)
print(odp33)
odpu3 = input("Odpowiedź:")

print("Twoje odpowiedzi to:")
print("Imie:"+imie)
print("Nazwisko:"+nazwisko)
print(pytanie1)
if odpu1 == "1" :
    print(odp11)
if odpu1 == "2":
    print(odp12)
if odpu1 == "3" :
    print(odp13)
print(pytanie2)
if odpu2 == "1" :
    print(odp21)
if odpu2 == "2" :
    print(odp21)
if odpu2 == "3" :
    print(odp21)
print(pytanie3)
if odpu3 == "1" :
    print(odp31)
if odpu3 == "2" :
    print(odp31)
if odpu3 == "3" :
    print(odp31)



