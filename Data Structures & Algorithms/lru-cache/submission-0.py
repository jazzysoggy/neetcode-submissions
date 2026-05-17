class Node:
    def __init__(self, key = 0, val = 0):
        self.nex = None
        self.pre = None
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.first = Node()
        self.last = Node()
        self.first.nex = self.last
        self.last.pre = self.first
        self.track = {}

    def add(self, node: Node):
        previous = self.last.pre

        previous.nex = node
        node.pre = previous

        node.nex = self.last
        self.last.pre = node

    def delete(self, key: int):

        nex = self.track[key].nex
        prev = self.track[key].pre

        nex.pre = prev
        prev.nex = nex

        del self.track[key]

    def get(self, key: int) -> int:
        if key not in self.track:
            return -1

        val = self.track[key].val

        self.delete(key)

        toAdd = Node(key, val)

        self.add(toAdd)

        self.track[key] = toAdd

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            self.delete(key)

        if len(self.track) == self.cap:
            toDel = self.first.nex.key

            self.delete(toDel)

        toAdd = Node(key, value)

        self.add(toAdd)

        self.track[key] = toAdd
