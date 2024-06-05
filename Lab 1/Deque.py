class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()

    def __str__(self):
        return str(self.items)

deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque)       
print(deque.remove_front())  
print(deque.remove_rear())   
print(deque)         