class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " -> "
            current = current.nextE
        result += "None"
        return result

    def get(self, e):
        current = self.head
        while current is not None:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        previous = None
        while current is not None:
            if current.data == e:
                if previous is not None:
                    previous.nextE = current.nextE
                else:
                    self.head = current.nextE
                if current.nextE is None:
                    self.tail = previous
                self.size -= 1
                return
            previous = current
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)

        # Jeśli lista jest pusta, dodajemy nowy element jako jedyny element w liście.
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
        # Jeśli nie została podana funkcja, porównujemy elementy za pomocą operatora >=.
        elif func is None:
            # Jeśli wartość elementu jest większa lub równa niż wartość ostatniego elementu na liście,
            # dodajemy nowy element na końcu listy.
            if self.tail.data <= e:
                self.tail.nextE = new_element
                self.tail = new_element
                self.size += 1
            # Jeśli wartość elementu jest mniejsza lub równa niż wartość pierwszego elementu na liście,
            # dodajemy nowy element na początku listy.
            elif self.head.data >= e:
                new_element.nextE = self.head
                self.head = new_element
                self.size += 1
            # W innym przypadku przechodzimy przez listę, aż znajdziemy element większy lub równy
            # od nowego elementu i dodajemy go przed tym elementem.
            else:
                current = self.head
                previous = None
                while current is not None:
                    if current.data >= e:
                        previous.nextE = new_element
                        new_element.nextE = current
                        self.size += 1
                        return
                    previous = current
                    current = current.nextE
        # Jeśli została podana funkcja, sortujemy listę zgodnie z funkcją.
        else:
            current = self.head
            previous = None
            while current is not None:
                if func(current.data, e):
                    if previous is not None:
                        previous.nextE = new_element
                    else:
                        self.head = new_element
                    new_element.nextE = current
                    self.size += 1
                    return
                previous = current
                current = current.nextE
            # Jeśli nie znaleźliśmy elementu, do którego nowy element pasuje, dodajemy go na końcu listy.
            self.tail.nextE = new_element
            self.tail = new_element
            self.size += 1


if __name__ == "__main__":
    # Tworzymy listę i dodajemy na nią kilka elementów.
    ll = MyLinkedList()
    ll.append(2)
    ll.append(4)
    ll.append(6)
    ll.append(1)

    # Usuwamy element o wartości 4 z listy.
    ll.delete(4)

    # Wyświetlamy zawartość listy.
    print("Linked list: " + str(ll))
