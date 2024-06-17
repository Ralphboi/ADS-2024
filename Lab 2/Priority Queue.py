class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        max_index = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self._heapify_down(max_index)

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return result

    def get_max(self):
        return self.heap[0] if self.heap else None

    def remove(self, index):
        if index >= len(self.heap):
            return

        self.heap[index] = float('inf')
        self._heapify_up(index)
        self.extract_max()

    def change_priority(self, index, priority):
        old_priority = self.heap[index]
        self.heap[index] = priority

        if priority > old_priority:
            self._heapify_up(index)
        else:
            self._heapify_down(index)

    def is_empty(self):
        return len(self.heap) == 0

# Example:
pq = PriorityQueue()
pq.insert(3)
pq.insert(5)
pq.insert(9)
pq.insert(1)
pq.insert(4)

print("Max element:", pq.get_max())  
print("Extr max:", pq.extract_max())  
print("Max element after extraction:", pq.get_max())  
pq.change_priority(2, 10)
print("Max element after change:", pq.get_max()) 
pq.remove(1)
print("Max element after removal:", pq.get_max())  
print("Is priority queue empty?", pq.is_empty())  
