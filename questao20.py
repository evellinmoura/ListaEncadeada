class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedBase:
    def __init__(self):
        self._header = DNode(None)
        self._trailer = DNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, item, predecessor, successor):
        new_node = DNode(item)
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node
    
    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        item = node.data
        node.prev = node.next = node.data = None
        return item
    
    def add_first(self, item):
        self._insert_between(item, self._header, self._header.next)
    
    def add_last(self, item):
        self._insert_between(item, self._trailer.prev, self._trailer)
    
    def reverse(self):
        current = self._header
        
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self._header.next
        while current != self._trailer:
            items.append(str(current.data))
            current = current.next
        return f"[{' <-> '.join(items)}]"


print("=" * 60)
print("MÉTODO REVERSE EM LISTA DUPLAMENTE ENCADEADA")
print("=" * 60)

while True:
    print("\nDigite valores (separados por espaço) ou 'sair':")
    entrada = input("→ ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    lista = DoublyLinkedBase()
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add_last(int(valor))
            except:
                lista.add_last(valor)
    
    if lista.is_empty():
        print("Lista esta vazia")
        continue
    
    print(f"\nLista original: {lista}")
    print(f"Tamanho: {len(lista)}")
    
    lista.reverse()
    
    print(f"\nLista invertida: {lista}")
    print(f"Tamanho: {len(lista)}")
    print("-" * 60)