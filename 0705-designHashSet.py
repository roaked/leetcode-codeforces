
"""Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing."""


class MyHashSet:

    def __init__(self):
        self.a = {}

    def add(self, key: int) -> None:
        self.a[key] = 1

    def remove(self, key: int) -> None:
        self.a[key] = 0

    def contains(self, key: int) -> bool:
        return self.a.get(key,0) != 0     

# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    
MyHashSet().add(key=1)     # set = [1]
MyHashSet().add(key=2)     # set = [1, 2]
MyHashSet().contains(key=1) # return True
MyHashSet().contains(key=3) # return False, (not found)
MyHashSet().add(key=2)     # set = [1, 2]
MyHashSet().contains(key=2) # return True
MyHashSet().remove(key=2)   # set = [1]
MyHashSet().contains(key=2) # return False, (already removed)
