#Zadanie 1 (4pkt):
#Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

iterator = ListIterator(lista1)
wynik1 = ''.join(str(element) for element in iterator)

print(wynik1)

#Zadanie2: (4pkt)
#Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
#listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
#reguła gry w FizzBuzz:
#Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
#Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
#Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    #zamiast pass wstaw swój kod!
    return ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, n + 1)]
wynik2 = fizbuzz(16)
print(wynik2)

#Zadanie 3 (4pkt):
#Napisz generator zwracający n wyrazów ciągu Lucasa
#do wyniku zapisz 6 element tego ciągu.

def lucas_numbers(n):
    a, b = 2, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

generator = lucas_numbers(6)
for number in generator:
    wynik3 = number

print(wynik3)

#Zadanie4 (4pkt):
#Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
#Do przechowywania znaków kodu javy z pliku Main.java.
class Stack:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size
    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            raise IndexError("Stack overflow")
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __iter__(self):
        return self
    def __next__(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise StopIteration

obiekt = Stack(max_size=200)

with open("Main.java", "r") as file:
    java_code = file.read()


for char in java_code:
    obiekt.push(char)


#następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
#ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
wynik4 = obiekt.size()
print(wynik4)

#Zadanie 5 (4pkt):
#Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
#funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    stack = kod_o

    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]

    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for char in stack:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != bracket_pairs[char]:
                return False

    return stack.is_empty()
wynik5 = validation(kod_o=obiekt)
print(wynik5)







