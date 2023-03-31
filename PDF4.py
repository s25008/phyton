#ZAD1
def panel_calc(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu):
    powierzchnia_pomieszczenia = (dlugosc_podlogi * szerokosc_podlogi) * 1.1
    powierzchnia_panela = dlugosc_panela * szerokosc_panela
    ilosc_paneli = powierzchnia_pomieszczenia / powierzchnia_panela
    ilosc_opakowan = ilosc_paneli / ilosc_paneli_w_opakowaniu
    return ilosc_opakowan

print("Potrzeba : " + str(panel_calc(5, 4, 1, 0.5, 10)))


#ZAD2
def czy_pierwsza(*liczby):
    wynik = []
    for liczba in liczby:
        if liczba < 2:
            wynik.append(f"{liczba} is not prime")
        elif liczba == 2:
            wynik.append(f"{liczba} is prime number")
        else:
            pierwsza = True
            for i in range(2, int(liczba ** 0.5) + 1):
                if liczba % i == 0:
                    pierwsza = False
                    break
            if pierwsza:
                wynik.append(f"{liczba} is prime number")
            else:
                wynik.append(f"{liczba} is not prime")
    return wynik


print(czy_pierwsza(2, 3, 4, 5, 6, 7, 8, 9, 10))



#ZAD3

def cezar(slowo, klucz, alfabet='abcdefghijklmnopqrstuvwxyz'):
    szyfr = ''
    klucz %= len(alfabet)
    for litera in slowo:
        if litera.lower() in alfabet:
            index = alfabet.find(litera.lower())
            if litera.isupper():
                szyfr += alfabet[(index + klucz) % len(alfabet)].upper()
            else:
                szyfr += alfabet[(index + klucz) % len(alfabet)]
        else:
            szyfr += litera
    return szyfr


print(cezar('Ala ma kota!', 3))
