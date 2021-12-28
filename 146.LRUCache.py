class Node:
    def __init__(self, key = None, value = None, next = None, prev = None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity_ = capacity
        self.cache_ = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size_ = 0
        
    def get(self, key: int) -> int:

        if key not in self.cache_:
            return -1
        
        self.move_to_front(key)
        
        return self.cache_[key].value

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache_:
            self.move_to_front(key)
            self.cache_[key].value = value
        
        else:
            node = Node(key = key,value=value)
            if self.size_ < self.capacity_:
                self.cache_[key] = node
                node.next = self.head.next
                self.head.next = node
                node.next.prev = node
                node.prev = self.head
                self.size_ += 1
            else:
                last = self.tail.prev
                last.prev.next = self.tail
                self.tail.prev = last.prev
                del self.cache_[last.key]
                self.cache_[key] = node
                node.next = self.head.next
                self.head.next = node
                node.next.prev = node
                node.prev = self.head

    def move_to_front(self, key)-> None:
        
        node = self.cache_[key]
        
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
        node.next = self.head.next
        self.head.next = node
        
        node.next.prev = node
        node.prev = self.head
        
        return 
    
        
        
"compact form"

class Node:

    def __init__(self, key = None, value = None, next = None, prev = None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_ = {}
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache_:
            return -1
        self.__move_to_front(key)
        return self.cache_[key].value

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache_:
            self.__move_to_front(key)
            self.cache_[key].value = value
        else:
            cur = Node(key = key, value = value)
            self.cache_[key] = cur
            if self.size < self.capacity:
                self.size += 1
            else:
                last = self.tail.prev
                del self.cache_[last.key]
                last.prev.next = self.tail
                self.tail.prev = last.prev   
            self.__add_to_head(cur)
    
    def __move_to_front(self, key):
        
        cur = self.cache_[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.__add_to_head(cur)
    
    def __add_to_head(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head