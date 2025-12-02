class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, max_size=5):
        self._head = None
        self._size = 0
        self._max_size = max_size

    def is_empty(self):
        return self._head is None

    def add(self, item):
        if self._size >= self._max_size:
            raise ValueError(f"A lista so pode conter no maximo {self._max_size} valores.")
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"[{' -> '.join(items)}]"

    def size(self):
        return self._size


def encontra_penultimo(lista):
    if lista._head is None:
        raise ValueError("Lista vazia")
    if lista._head.next is None:
        raise ValueError("Lista tem apenas um elemento")
    current = lista._head
    while current.next.next is not None:
        current = current.next
    return current.data


if __name__ == "__main__":
    lista = LinkedList(max_size=5)

    print("Insira no maximo 5 valores inteiros.")
    while lista.size() < 5:
        entrada = input(f"Valor {lista.size()+1}: ").strip()
        if entrada == "":
            break
        try:
            valor = int(entrada)
            lista.add(valor)
        except ValueError as e:
            print(f"Erro: {e}")
        else:
            print(f"Adicionado: {valor}  -> {lista}")

    print(f"\nLista final: {lista}")

    try:
        penultimo = encontra_penultimo(lista)
        print(f"Penultimo no: {penultimo}")
    except ValueError as e:
        print(f"Erro: {e}")