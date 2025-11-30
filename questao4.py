"""Forneca um m ́etodo recursivo para remover todos os elementos de uma pilha."""
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
    
    def __str__(self):
        return str(self._data)
    
    def __len__(self):
        return len(self._data)


def recursive_clear(S):
    """Remove recursivamente todos os elementos da pilha S"""
    if not S.is_empty():
        S.pop()
        recursive_clear(S)


# Teste
print("=== METODO RECURSIVO PARA LIMPAR PILHA ===\n")

S = ArrayStack()

# Adiciona elementos
for i in [10, 20, 30, 40, 50]:
    S.push(i)

print(f"Pilha antes:  {S}")
print(f"Tamanho: {len(S)}")

# Remove recursivamente
recursive_clear(S)

print(f"\nPilha depois: {S}")
print(f"Tamanho: {len(S)}")
print(f"Ta vazia? {S.is_empty()}")

# Teste com outra pilha
print("\n" + "="*40)
print("Outro exemplo:")
print("="*40)

S2 = ArrayStack()
for char in ['A', 'B', 'C', 'D']:
    S2.push(char)

print(f"\nPilha S2 antes:  {S2}")
recursive_clear(S2)
print(f"Pilha S2 depois: {S2}")