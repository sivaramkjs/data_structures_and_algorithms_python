class MyHashTable:
    def __init__(self, size):
        # [[]] * size -> this will also create a list with 50 empty list elements. However, all inner lists will reference the same list object.
        # As a result, all elements will contain the same list.
        self.data = [[] for _ in range(size)]

    def __hash_func(self, key):
        hash_val = 0
        for i in range(len(key)):
            hash_val = (hash_val + ord(key[i]) * i) % len(self.data)
        return hash_val

    def insert(self, key, val):  # O(1)
        key_hash = self.__hash_func(key)
        # print(self.data)
        self.data[key_hash].append([key, val])
        print(self.data)

    def get(self, key):  # O(1) most times, O(n) in case of many collisions
        key_hash = self.__hash_func(key)
        current_bucket = self.data[key_hash]
        if not current_bucket:
            return None
        for item in current_bucket:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):  # O(n)
        keys = []
        for item in self.data:
            if item:
                keys.append(item[0][0])
        return keys

    def values(self):  # O(n)
        values = []
        for item in self.data:
            if item:
                values.append(item[0][1])
        return values


hash_table = MyHashTable(50)
hash_table.insert('grapes', 10000)
hash_table.insert('apples', 100001)
hash_table.insert('mangoes', 100002)
print(hash_table.get('apples'))
print(hash_table.keys())
print(hash_table.values())
