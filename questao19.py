class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self._header = DNode(None)
        self._trailer = DNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def add(self, item):
        new_node = DNode(item)
        predecessor = self._trailer.prev
        new_node.prev = predecessor
        new_node.next = self._trailer
        predecessor.next = new_node
        self._trailer.prev = new_node
        self._size += 1
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self._header.next
        while current != self._trailer:
            items.append(str(current.data))
            current = current.next
        return f"[{' <-> '.join(items)}]"
    
    def __len__(self):
        return self._size


def remover_duplicatas(lista):
    if lista.is_empty():
        return
    
    vistos = set()
    current = lista._header.next
    
    while current != lista._trailer:
        if current.data in vistos:
            predecessor = current.prev
            successor = current.next
            predecessor.next = successor
            successor.prev = predecessor
            lista._size -= 1
            current = successor
        else:
            vistos.add(current.data)
            current = current.next


print("=" * 60)
print("REMOVER DUPLICATAS EM LISTA DUPLAMENTE ENCADEADA")
print("=" * 60)

while True:
    print("\nDigite valores (separados por espaço) ou 'sair':")
    entrada = input("→ ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    lista = DoublyLinkedList()
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                lista.add(valor)
    
    if lista.is_empty():
        print("Lista esta vazia")
        continue
    
    print(f"\nLista original: {lista}")
    print(f"Tamanho: {len(lista)}")
    
    remover_duplicatas(lista)
    
    print(f"\nLista sem duplicatas: {lista}")
    print(f"Tamanho: {len(lista)}")
    print("-" * 60)