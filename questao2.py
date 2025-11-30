"""Execute a seguinte série de operacoes de pilha, assumindo uma pilha inicialmente vazia:
push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7),
push(6), pop(), pop(), push(4), pop(), pop()."""""

class ArrayStack:
    """Implementacao de Pilha (Stack) usando array dinamico.
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
        """Verifica se a pilha ta vazia."""
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
        
        # Reduz o tamanho do array se necessário
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return item
    
    def top(self):
        """Retorna o elemento do topo sem remover ele."""
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
        """Retorna lista com elementos da pilha (base->topo)."""
        return [self._data[i] for i in range(self._size)]
    
    def __str__(self):
        """Representacao em string da pilha."""
        if self.is_empty():
            return "Stack: []"
        items = [str(self._data[i]) for i in range(self._size)]
        return f"Stack: [{', '.join(items)}] <- topo"


# execucao da sequencia de operacoes
print("=" * 70)
print("EXECUCAO DE OPERACOES NA PILHA")
print("=" * 70)

stack = ArrayStack()
operation_number = 0

def execute_and_show(operation, stack, op_num):
    """Executa uma operacao e mostra o resultado."""
    print(f"\n{op_num}. {operation}")
    
    if operation.startswith("push"):
        value = int(operation.split("(")[1].split(")")[0])
        stack.push(value)
        print(f"   → Empilhou: {value}")
    elif operation == "pop()":
        if not stack.is_empty():
            value = stack.pop()
            print(f"   → Desempilhou: {value}")
        else:
            print(f"   → Erro: pilha vazia")
    
    if stack.is_empty():
        print(f"   Estado: []")
    else:
        elements = stack.get_elements()
        print(f"   Estado: {elements} (topo: {stack.top()})")

# sequencia de operacoes
operations = [
    "push(5)", "push(3)", "pop()", "push(2)", "push(8)", 
    "pop()", "pop()", "push(9)", "push(1)", "pop()", 
    "push(7)", "push(6)", "pop()", "pop()", "push(4)", 
    "pop()", "pop()"
]

for i, op in enumerate(operations, 1):
    execute_and_show(op, stack, i)

print("\n" + "=" * 70)
print(f"ESTADO FINAL DA PILHA: {stack.get_elements() if not stack.is_empty() else '[]'}")
print(f"Pilha ta vazia: {stack.is_empty()}")
print("=" * 70)

# Resumo dos valores retornados por pop()
print("\n" + "=" * 70)
print("RESUMO DOS VALORES RETORNADOS POR pop():")
print("=" * 70)

stack2 = ArrayStack()
pop_results = []

for op in operations:
    if op.startswith("push"):
        value = int(op.split("(")[1].split(")")[0])
        stack2.push(value)
    elif op == "pop()":
        if not stack2.is_empty():
            pop_results.append(stack2.pop())

print(f"Valores retornados orddenados: {pop_results}")
print(f"Total de pop() executados: {len(pop_results)}")
print("=" * 70)