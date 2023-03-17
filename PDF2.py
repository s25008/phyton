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

