"""Execute a seguinte s ́erie de operacoes de deque, assumindo uma deque inicialmente vazia:
add first(4), add last(8), add last(9), add first(5), back(), delete first( ), delete last( ), add
last(7), first( ), last( ), add last(6), delete first( ), delete first( )."""

class ArrayDeque:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def add_first(self, item):
        self._data.insert(0, item)
    
    def add_last(self, item):
        self._data.append(item)
    
    def delete_first(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data.pop(0)
    
    def delete_last(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data.pop()
    
    def first(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data[0]
    
    def last(self):
        if self.is_empty():
            raise IndexError("deque vazio")
        return self._data[-1]
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        return f"[{', '.join(map(str, self._data))}]"


# execucao das operacoes
print("OPERACOES NO DEQUE\n")

deque = ArrayDeque()

operations = [
    "add_first(4)", "add_last(8)", "add_last(9)", "add_first(5)", 
    "last()", "delete_first()", "delete_last()", "add_last(7)", 
    "first()", "last()", "add_last(6)", "delete_first()", "delete_first()"
]

for i, op in enumerate(operations, 1):
    print(f"{i:2}. {op:18}", end="")
    
    if "add_first" in op:
        value = int(op.split("(")[1].split(")")[0])
        deque.add_first(value)
        print(f" → {deque}")
    
    elif "add_last" in op:
        value = int(op.split("(")[1].split(")")[0])
        deque.add_last(value)
        print(f" → {deque}")
    
    elif op == "delete_first()":
        value = deque.delete_first()
        estado = deque if not deque.is_empty() else "[]"
        print(f" → remove {value}, deque: {estado}")
    
    elif op == "delete_last()":
        value = deque.delete_last()
        estado = deque if not deque.is_empty() else "[]"
        print(f" → remove {value}, deque: {estado}")
    
    elif op == "first()":
        value = deque.first()
        print(f" → retorna {value}")
    
    elif op == "last()":
        value = deque.last()
        print(f" → retorna {value}")

print(f"\n{'='*50}")
print(f"Estado final: {deque}")
print(f"{'='*50}")
