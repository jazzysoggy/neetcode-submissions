class MyHashSet:

    def __init__(self):
        self.table = []

    def add(self, key: int) -> None:
        while len(self.table) - 1 < key:
            self.table.append(False)

        self.table[key] = True

    def remove(self, key: int) -> None:
        if len(self.table) - 1 < key or not self.table[key]:
            return
        
        self.table[key] = False

    def contains(self, key: int) -> bool:
        if len(self.table) - 1 < key or not self.table[key]:
            return False
        
        return self.table[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)