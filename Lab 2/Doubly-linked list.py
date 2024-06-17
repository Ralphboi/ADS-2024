class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, key):
        cur_node = self.head

        while cur_node:
            if cur_node.data == key:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                if cur_node == self.tail:
                    self.tail = cur_node.prev
                cur_node = None
                return
            cur_node = cur_node.next

    def delete_node_at_index(self, index):
        if index < 0:
            return

        cur_node = self.head
        count = 0

        while cur_node and count != index:
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        if cur_node.prev:
            cur_node.prev.next = cur_node.next
        if cur_node.next:
            cur_node.next.prev = cur_node.prev
        if cur_node == self.head:
            self.head = cur_node.next
        if cur_node == self.tail:
            self.tail = cur_node.prev
        cur_node = None

    def print_list(self):
        nodes = []
        cur_node = self.head
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        print(" <-> ".join(map(str, nodes)) + " <-> None")

    def print_list_reverse(self):
        nodes = []
        cur_node = self.tail
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.prev
        print(" <-> ".join(map(str, nodes)) + " <-> None")

# Example usage:
dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.print_list()  

dll.prepend("D")
dll.print_list()  

dll.delete_node("B")
dll.print_list()  

dll.delete_node_at_index(1)
dll.print_list()  

dll.print_list_reverse()  
