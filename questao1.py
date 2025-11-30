"Primeira questão:"
"Implemente as classes ArrayStack, ArrayQueue e ArrayDeque."

class ArrayStack:
    """Implementação da Pilha (Stack) usando array dinamico.
    Seguindo o princípio LIFO."""
    
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
        """Retorna o elemento do topo sem remover."""
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
    
    def __str__(self):
        """Representacao em string da pilha."""
        items = [str(self._data[i]) for i in range(self._size)]
        return f"Stack([{', '.join(items)}]) <- topo"


class ArrayQueue:
    """Implementação de Fila (Queue) usando array circular.
    Seguindo o princípio FIFO."""
    
    def __init__(self, capacity=10):
        """Inicializa a fila com capacidade inicial."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._capacity = capacity
    
    def __len__(self):
        """Retorna o numero de elementos na fila."""
        return self._size
    
    def is_empty(self):
        """Verificacao da fila vazia."""
        return self._size == 0
    
    def enqueue(self, item):
        """Adiciona um elemento no final da fila."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1
    
    def dequeue(self):
        """Remove e retorna o elemento da frente da fila."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        # Reduz o tamanho do array se necessário
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return item
    
    def first(self):
        """Retorna o elemento da frente sem remover ele."""
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self._data[self._front]
    
    def _resize(self, new_capacity):
        """Redimensiona o array interno."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_capacity
    
    def __str__(self):
        """Representação em string da fila."""
        items = []
        for i in range(self._size):
            items.append(str(self._data[(self._front + i) % self._capacity]))
        return f"Queue([{', '.join(items)}]) <- rear"


class ArrayDeque:
    """Implementação de Deque (Double-Ended Queue) usando array circular.
    Que permite a inserção e a remoção nas extremidades."""
    
    def __init__(self, capacity=10):
        """Inicializa o deque com capacidade inicial."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._capacity = capacity
    
    def __len__(self):
        """Retorna o numero de elementos no deque."""
        return self._size
    
    def is_empty(self):
        """Verifica se o deque ta vazio."""
        return self._size == 0
    
    def add_first(self, item):
        """Adiciona um elemento no inicio do deque."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        self._front = (self._front - 1) % self._capacity
        self._data[self._front] = item
        self._size += 1
    
    def add_last(self, item):
        """Adiciona um elemento no final do deque."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1
    
    def delete_first(self):
        """Remove e retorna o elemento do inicio do deque."""
        if self.is_empty():
            raise IndexError("delete_first from empty deque")
        
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return item
    
    def delete_last(self):
        """Remove e retorna o elemento do final do deque."""
        if self.is_empty():
            raise IndexError("delete_last from empty deque")
        
        rear = (self._front + self._size - 1) % self._capacity
        item = self._data[rear]
        self._data[rear] = None
        self._size -= 1
        
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return item
    
    def first(self):
        """Retorna o primeiro elemento sem removê-lo."""
        if self.is_empty():
            raise IndexError("first from empty deque")
        return self._data[self._front]
    
    def last(self):
        """Retorna o último elemento sem remover ele."""
        if self.is_empty():
            raise IndexError("last from empty deque")
        rear = (self._front + self._size - 1) % self._capacity
        return self._data[rear]
    
    def _resize(self, new_capacity):
        """Redimensiona o array interno."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = new_capacity
    
    def __str__(self):
        """Representaçao em string do deque."""
        items = []
        for i in range(self._size):
            items.append(str(self._data[(self._front + i) % self._capacity]))
        return f"Deque([{', '.join(items)}])"


# Exemplos de uso
if __name__ == "__main__":
    print("=== ArrayStack ===")
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(f"Topo: {stack.top()}")
    print(f"Pop: {stack.pop()}")
    print(stack)
    
    print("\n=== ArrayQueue ===")
    queue = ArrayQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(f"Primeiro: {queue.first()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(queue)
    
    print("\n=== ArrayDeque ===")
    deque = ArrayDeque()
    deque.add_last(10)
    deque.add_first(5)
    deque.add_last(20)
    deque.add_first(1)
    print(deque)
    print(f"Primeiro: {deque.first()}, Último: {deque.last()}")
    print(f"Delete first: {deque.delete_first()}")
    print(f"Delete last: {deque.delete_last()}")
    print(deque)