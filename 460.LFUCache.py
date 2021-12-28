class Node:
    
    def __init__(self, key = None, value = None, freq = 1, next = None, prev = None) -> None:
        self.key = key
        self.value = value
        self.freq = 1
        self.next = next
        self.prev = prev
        
class Linkedlist:
    
    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
        
    def append(self, node):
        node.next = self._head.next
        self._head.next = node
        node.next.prev = node
        node.prev = self._head
        self._size += 1
    
    def pop(self, node = None):
        if not self._size:
            return  

        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = self._tail.prev
            node.prev.next = self._tail
            self._tail.prev = node.prev
        self._size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._cache = {}
        self._freq = collections.defaultdict(Linkedlist)
        self.__minfreq = 0

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self.__update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return 
        
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self.__update(node)
        else:
            node = Node(key = key, value = value)
            if self._size == self._capacity:
                old = self._freq[self.__minfreq].pop()
                del self._cache[old.key]
                self._size -= 1
                if self._freq[self.__minfreq]._size == 0:
                    del self._freq[self.__minfreq]

            self._cache[key] = node
            self._freq[node.freq].append(node)
            self._size += 1
            self.__minfreq = 1
    
    
    def __update(self, node):
        nodelist = self._freq[node.freq]
        nodelist.pop(node)
        if self.__minfreq == node.freq and nodelist._size == 0:
            self.__minfreq += 1
            del self._freq[node.freq]
        node.freq += 1
        self._freq[node.freq].append(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)