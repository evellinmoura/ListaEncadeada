class ArrayStack:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pilha vazia")
        return self._data.pop()


def reverse_list(lst):
  
    stack = ArrayStack()
    
    # empilha todos os elementos
    for element in lst:
        stack.push(element)
    
    # desempilha de volta para a lista
    for i in range(len(lst)):
        lst[i] = stack.pop()


# testes
print("FUNÇÃO PARA INVERTER LISTA USANDO PILHA\n")
print("=" * 50)

# teste 1: lista de números
lista1 = [1, 2, 3, 4, 5]
print(f"Lista original: {lista1}")
reverse_list(lista1)
print(f"Lista invertida: {lista1}")

print("\n" + "=" * 50)

# teste 2: lista de strings
lista2 = ["Python", "Java", "C++", "JavaScript"]
print(f"Lista original: {lista2}")
reverse_list(lista2)
print(f"Lista invertida: {lista2}")

print("\n" + "=" * 50)

# teste 3: lista de caracteres
lista3 = list("ESTRUTURA")
print(f"Lista original: {lista3}")
reverse_list(lista3)
print(f"Lista invertida: {lista3}")
print(f"String invertida: {''.join(lista3)}")

print("\n" + "=" * 50)

# Teste 4: Lista vazia
lista4 = []
print(f"Lista vazia: {lista4}")
reverse_list(lista4)
print(f"Depois da inversão: {lista4}")

print("\n" + "=" * 50)

# teste 5: lista com um elemento
lista5 = [42]
print(f"Lista com 1 elemento: {lista5}")
reverse_list(lista5)
print(f"Depois da inversão: {lista5}")

print("\n" + "=" * 50)