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


def separar_positivos_negativos(lista):
    positivos = LinkedList()
    negativos = LinkedList()
    
    current = lista._head
    while current is not None:
        if current.data > 0:
            positivos.add(current.data)
        elif current.data < 0:
            negativos.add(current.data)
        current = current.next
    
    return positivos, negativos


print("=" * 60)
print("SEPARAR NUMEROS POSITIVOS E NEGATIVOS")
print("=" * 60)

while True:
    print("\nDigite numeros (separados por espaço) ou 'sair':")
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
                print(f"'{valor}' não é um numero valido, ignorando...")
    
    if lista.is_empty():
        print("Lista esta vazia")
        continue
    
    print(f"\nLista original: {lista}")
    
    positivos, negativos = separar_positivos_negativos(lista)
    
    print(f"Lista positivos: {positivos}")
    print(f"Lista negativos: {negativos}")
    print("-" * 60)