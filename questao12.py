class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        new_node = Node(value, next=self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._top.value

    def __len__(self):
        return self._size