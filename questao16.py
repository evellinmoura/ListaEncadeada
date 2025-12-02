class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self._tail = None
    
    def is_empty(self):
        return self._tail is None
    
    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self._tail = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
            self._tail = new_node
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self._tail.next
        start = current
        while True:
            items.append(str(current.data))
            current = current.next
            if current == start:
                break
        return f"[{' -> '.join(items)} -> (circular)]"


def conta_nos(lista):
    if lista._tail is None:
        return 0
    
    count = 1
    current = lista._tail.next
    while current != lista._tail:
        count += 1
        current = current.next
    
    return count


print("=" * 60)
print("CONTAR NOS EM LISTA CIRCULAR")
print("=" * 60)

while True:
    print("\nDigite valores (separados por espaço) ou 'sair':")
    entrada = input("→ ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    lista = CircularLinkedList()
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                lista.add(valor)
    
    print(f"\nLista: {lista}")
    num_nos = conta_nos(lista)
    print(f"Numero de nos: {num_nos}")
    print("-" * 60)