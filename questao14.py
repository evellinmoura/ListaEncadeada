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
    
    def __len__(self):
        return self._size


def concatenar(L, M):
    if L.is_empty():
        L._head = M._head
        L._size = M._size
    else:
        current = L._head
        while current.next is not None:
            current = current.next
        current.next = M._head
        L._size += M._size
    
    M._head = None
    M._size = 0


print("=" * 60)
print("CONCATENACAO DE LISTAS ENCADEADAS")
print("=" * 60)

while True:
    print("\n--- LISTA L ---")
    L = LinkedList()
    entrada = input("Digite valores para L (separados por espaco): ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                L.add(int(valor))
            except:
                L.add(valor)
    
    print("\n--- LISTA M ---")
    M = LinkedList()
    entrada = input("Digite valores para M (separados por espaco): ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                M.add(int(valor))
            except:
                M.add(valor)
    
    print("\n" + "=" * 60)
    print("ANTES DA CONCATENACAO:")
    print(f"L: {L} (tamanho: {len(L)})")
    print(f"M: {M} (tamanho: {len(M)})")
    
    concatenar(L, M)
    
    print("\nDEPOIS DA CONCATENACAO:")
    print(f"L: {L} (tamanho: {len(L)})")
    print(f"M: {M} (tamanho: {len(M)})")
    print("=" * 60)
    
    continuar = input("\nDeseja fazer outra concatenacao? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando...")
        break