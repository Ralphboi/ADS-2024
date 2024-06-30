class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value])

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key {key} not found")

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        return str(self.table)

# Example
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)

    print("Initial table:")
    print(ht)

    print("Search for 'banana':", ht.search("banana"))
    
    ht.remove("banana")
    
    print("Table after removing 'banana':")
    print(ht)

    try:
        print("Search for 'banana':", ht.search("banana"))
    except KeyError as e:
        print(e)
