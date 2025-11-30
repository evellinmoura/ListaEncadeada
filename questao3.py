"""Implemente uma função com assinatura transfer(S, T) que transfira todos os elementos da
pilha S para a pilha T, de modo que o elemento que come ̧ca no topo de S seja o primeiro a
ser inserido em T, e o elemento na parte inferior de S termine no topo de T."""

class ArrayStack:
    """Implementação de Pilha (Stack) usando array dinamico.
    Segue o princípio LIFO."""
    
    def __init__(self, capacity=10):
        """Inicializa a pilha com capacidade inicial."""
        self._data = [None] * capacity
        self._size = 0
        self._capacity = capacity
    
    def __len__(self):
        """Retorna o numero de elementos na pilha."""
        return self._size
    
    def is_empty(self):
        """Verifica se a pilha esta  vazia."""
        return self._size == 0
    
    def push(self, item):
        """Adiciona um elemento no topo da pilha."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = item
        self._size += 1
    
    def pop(self):
        """Remove e retorna o elemento do topo da pilha."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return item
    
    def top(self):
        """Retorna o elemento do topo sem removê-lo."""
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._data[self._size - 1]
    
    def _resize(self, new_capacity):
        """Redimensiona o array interno."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
    
    def get_elements(self):
        """Retorna lista com elementos da pilha (base -> topo)."""
        return [self._data[i] for i in range(self._size)]
    
    def __str__(self):
        """Representação em string da pilha."""
        if self.is_empty():
            return "[]"
        items = [str(self._data[i]) for i in range(self._size)]
        return f"[{', '.join(items)}] <- topo"


def transfer(S, T):
    """
    Transfere todos os elementos da pilha S para a pilha T.
    
    O elemento que está no topo de S será o primeiro a ser inserido em T,
    e o elemento na base de S terminará no topo de T.
    
    Resultado: A ordem dos elementos é invertida.
    - S fica vazia
    - T recebe os elementos em ordem inversa
    
    Parâmetros:
        S: Pilha de origem (sera esvaziada)
        T: Pilha de destino (receberá os elementos)
    
    Complexidade: O(n) onde n é o número de elementos em S
    """
    while not S.is_empty():
        element = S.pop()
        T.push(element)


# demosntraçao da função transfer
print("=" * 70)
print("DEMONSTRAÇÃO DA FUNÇÃO transfer(S, T)")
print("=" * 70)

# criando e populando a pilha S
S = ArrayStack()
print("\n1. Criando pilha S e adicionando elementos:")
elements = [1, 2, 3, 4, 5]
for elem in elements:
    S.push(elem)
    print(f"   push({elem})")

print(f"\nPilha S: {S}")
print(f"   Base -> Topo: {S.get_elements()}")
print(f"   Topo de S: {S.top()}")

# criando pilha T vazia
T = ArrayStack()
print(f"\n2. Pilha T (inicialmente vazia): {T}")

# executando a transferencia
print(f"\n3. Executando transfer(S, T)...")
print("   Operações realizadas:")

# versao com log para mostrar o processo
temp_s = ArrayStack()
for elem in S.get_elements():
    temp_s.push(elem)

step = 1
while not temp_s.is_empty():
    elem = temp_s.pop()
    T.push(elem)
    print(f"   Passo {step}: pop({elem}) de S → push({elem}) em T")
    print(f"            S: {temp_s}, T: {T}")
    step += 1

# limpando S original
while not S.is_empty():
    S.pop()

print(f"\n4. Resultado após transfer(S, T):")
print(f"   Pilha S: {S} (vazia)")
print(f"   Pilha T: {T}")
print(f"   Base -> Topo de T: {T.get_elements()}")
print(f"   Topo de T: {T.top()}")


# exemplo com strings tambem 
print("\n" + "=" * 70)
print("EXEMPLO ADICIONAL COM STRINGS:")
print("=" * 70)

S2 = ArrayStack()
words = ["Python", "Java", "C++", "JavaScript"]
print(f"\nPilha S2 original: ", end="")
for word in words:
    S2.push(word)
print(S2)

T2 = ArrayStack()
transfer(S2, T2)

print(f"Pilha S2 depois de transfer: {S2}")
print(f"Pilha T2 depois de transfer: {T2}")
print(f"\nOrdem invertida: {' -> '.join(T2.get_elements()[::-1])}")
print("=" * 70)