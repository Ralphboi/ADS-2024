class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)        
print(stack.pop()) 
print(stack)        
