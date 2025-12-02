class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
    
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
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"[{' -> '.join(items)}]"


def conta_nos_recursivo(node):
    if node is None:
        return 0
    return 1 + conta_nos_recursivo(node.next)


def conta_nos(lista):
    return conta_nos_recursivo(lista._head)


print("=" * 60)
print("CONTAGEM RECURSIVA DE NOS")
print("=" * 60)

while True:
    print("\nDigite valores (separados por espaço) ou 'sair':")
    entrada = input("→ ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    lista = LinkedList()
    
    if entrada.strip():
        for valor in entrada.split():
            try:
                lista.add(int(valor))
            except:
                lista.add(valor)
    
    print(f"\nLista: {lista}")
    num_nos = conta_nos(lista)
    print(f"Número de nos: {num_nos}")
    print("-" * 60)