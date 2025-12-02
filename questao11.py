from collections import deque

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.data = deque()
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.popleft()
    
    def is_empty(self):
        return len(self.data) == 0


def eh_palindromo(string):
    stack = Stack()
    queue = Queue()
    
  
    for char in string:
        if char != " ": 
            stack.push(char.lower())
            queue.enqueue(char.lower())
    
    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    
    return True

texto = input("Digite uma palavra ou frase: ")

if eh_palindromo(texto):
    print("É palíndromo")
else:
    print("Nao é palíndromo.")