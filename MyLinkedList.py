class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

#ZAD1
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return ' -> '.join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        previous = None
        while current:
            if current.data == e:
                if previous:
                    previous.nextE = current.nextE
                else:
                    self.head = current.nextE
                if current == self.tail:
                    self.tail = previous
                self.size -= 1
                return
            previous = current
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        if self.size == 0:
            self.head = new_element
            self.tail = new_element
        elif func is None:
            if e >= self.tail.data:
                self.tail.nextE = new_element
                self.tail = new_element
            elif e <= self.head.data:
                new_element.nextE = self.head
                self.head = new_element
            else:
                current = self.head
                while current.nextE and e > current.nextE.data:
                    current = current.nextE
                new_element.nextE = current.nextE
                current.nextE = new_element
        else:
            current = self.head
            previous = None
            while current and not func(e, current.data):
                previous = current
                current = current.nextE
            if previous:
                previous.nextE = new_element
            else:
                self.head = new_element
            new_element.nextE = current
            if current is None:
                self.tail = new_element
        self.size += 1


# Tworzenie instancji listy
my_list = Lista()

# Dodawanie elementów
my_list.append(5)
my_list.append(2)
my_list.append(8)
my_list.append(1)
my_list.append(4)

# Wyświetlanie listy
print(my_list)

# Pobieranie elementu
element = my_list.get(2)
if element:
    print(element.data)
else:
    print("Element not found")

# Usuwanie elementu
my_list.delete(4)
print(my_list)