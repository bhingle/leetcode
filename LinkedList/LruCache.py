class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #dummy left and right node
        #left - lru
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {} #map key to node

    #remove from list
    #previous and next node are calculated based on the node parameter sent
    def remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    #insert at the right
    def insert(self,node):
        n = self.right
        p = self.right.prev
        p.next = node
        n.prev = node
        node.prev = p
        node.next = n
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)