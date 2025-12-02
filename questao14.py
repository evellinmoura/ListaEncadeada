class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def is_empty(self):
        return self._head is None
    
    def add(self, item):
        if self._size >= 5:
            raise ValueError("A lista apenas pode conter no maximo 5 valores.")
        
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
    print("ALGORITMO PARA ENCONTRAR PENULTIMO NO\n")
    
    lista = LinkedList()
    
    
    try:
        lista.add(10)
        lista.add(20)
        lista.add(30)
        lista.add(40)
        lista.add(50)
        lista.add(60)  
    except ValueError as e:
        print(f"Erro ao inserir: {e}")
    
    print(f"Lista: {lista}")
    
    penultimo = encontra_penultimo(lista)
    print(f"Penultimo no: {penultimo}")