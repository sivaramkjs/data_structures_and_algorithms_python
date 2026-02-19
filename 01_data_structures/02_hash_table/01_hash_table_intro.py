# Hash tables are hash-based data structures (DS) that store key-value pairs.
# Different languages have different hash-based data structures. E.g., Python - Dictionary, Java - Hash Map, JavaScript - Object
# In Python, we also have Set DS which is a hash set that stores only unique values.

# Every hash-based DS will have a hash function to compute a hash value for a given key and stores the key-value pair based on the computed hash.
# It would be mostly one-way hashing i.e., "key" leads to "hash" but vice versa.
# Hash function must be idempotent i.e., always return the same hash value for a same key

# Time Complexity of operations:
# Insert - O(1)
# Lookup - O(1)
# Search - O(1)
# Delete - O(1)

# Hash Collisions:
# 1. When different keys generate same hash then it will result in a "hash collision" to store the multiple keys at the same hash-based location in the hash table.
# 2. Because of this, occasionally all operations can take O(n) in case of a collision due to traversing through all the collision chain then finding an element or insertion slot.

# Collision resolution techniques: (https://en.wikipedia.org/wiki/Hash_table#Collision_resolution)
# 1. Separate chaining
# 2. Open addressing
