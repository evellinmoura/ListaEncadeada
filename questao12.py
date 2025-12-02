class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item
    
    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._head.data
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"Stack: [{', '.join(reversed(items))}] <- topo"


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return item
    
    def first(self):
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self._head.data
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        items = []
        current = self._head
        while current:
            items.append(str(current.data))
            current = current.next
        return f"Queue: [{', '.join(items)}]"


class CircularQueue:
    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self._tail = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        head = self._tail.next
        item = head.data
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next
        self._size -= 1
        return item
    
    def first(self):
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self._tail.next.data
    
    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail.next
    
    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        items = []
        current = self._tail.next
        for _ in range(self._size):
            items.append(str(current.data))
            current = current.next
        return f"CircularQueue: [{', '.join(items)}]"


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedDeque:
    def __init__(self):
        self._header = DNode(None)
        self._trailer = DNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, item, predecessor, successor):
        new_node = DNode(item)
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node
    
    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        item = node.data
        node.prev = node.next = node.data = None
        return item
    
    def add_first(self, item):
        self._insert_between(item, self._header, self._header.next)
    
    def add_last(self, item):
        self._insert_between(item, self._trailer.prev, self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise IndexError("delete_first from empty deque")
        return self._delete_node(self._header.next)
    
    def delete_last(self):
        if self.is_empty():
            raise IndexError("delete_last from empty deque")
        return self._delete_node(self._trailer.prev)
    
    def first(self):
        if self.is_empty():
            raise IndexError("first from empty deque")
        return self._header.next.data
    
    def last(self):
        if self.is_empty():
            raise IndexError("last from empty deque")
        return self._trailer.prev.data
    
    def __str__(self):
        if self.is_empty():
            return "Deque: []"
        items = []
        current = self._header.next
        while current != self._trailer:
            items.append(str(current.data))
            current = current.next
        return f"Deque: [{', '.join(items)}]"


if __name__ == "__main__":
    print("=== LinkedStack ===")
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(f"Pop: {stack.pop()}")
    print(stack)
    
    print("\n=== LinkedQueue ===")
    queue = LinkedQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(f"Dequeue: {queue.dequeue()}")
    print(queue)
    
    print("\n=== CircularQueue ===")
    cqueue = CircularQueue()
    cqueue.enqueue(10)
    cqueue.enqueue(20)
    cqueue.enqueue(30)
    print(cqueue)
    cqueue.rotate()
    print(f"Apos o rotate: {cqueue}")
    print(f"Dequeue: {cqueue.dequeue()}")
    print(cqueue)
    
    print("\n=== LinkedDeque ===")
    deque = LinkedDeque()
    deque.add_last(10)
    deque.add_first(5)
    deque.add_last(20)
    deque.add_first(1)
    print(deque)
    print(f"Delete first: {deque.delete_first()}")
    print(f"Delete last: {deque.delete_last()}")
    print(deque)