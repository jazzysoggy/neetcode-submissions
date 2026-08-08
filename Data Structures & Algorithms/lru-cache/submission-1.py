class Node:
    def __init__(self, key = 0, value = 0):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.first = Node()
        self.last = Node()

        self.first.next = self.last
        self.last.prev = self.first

        self.tracker = {}

        self.capacity = capacity

    def remove(self, key):
        if not key in self.tracker:
            return

        node = self.tracker[key]

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        del self.tracker[key]

    def insert(self, key, value):
        node = Node(key, value)
        self.tracker[key] = node

        ogNext = self.first.next

        self.first.next = node
        ogNext.prev = node

        node.next = ogNext
        node.prev = self.first
        

    def get(self, key: int) -> int:
        if not key in self.tracker:
            return -1

        value = self.tracker[key].value
        self.remove(key)
        self.insert(key, value)
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.tracker:
            self.remove(key)

        self.insert(key, value)

        if len(self.tracker) > self.capacity:
            self.remove(self.last.prev.key)
        
