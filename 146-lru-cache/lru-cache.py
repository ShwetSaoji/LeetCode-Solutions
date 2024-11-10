class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hmap = {}
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        node.next, node.prev = nxt, prev
        prev.next = self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
            
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])
        if len(self.hmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)