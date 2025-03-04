"""
Problem: Design HashSet
"""

# Approach: Use a list of buckets to store the elements. Each bucket is a linked list. The hash function is used to
# calculate the index of the bucket. The add, remove, and contains functions are implemented using the linked list
# operations.

# Time Complexity:
# add: O(1)
# remove: O(n/k) where n is the number of elements and k is the number of buckets
# contains: O(n/k) where n is the number of elements and k is the number of buckets


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            new_node = Node(value, self.head.next)
            self.head.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                return True

            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
