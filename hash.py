# hash set with linked list

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.range = 769 # depends on the range, biggest prime that less than the range
        self.bucketarray = [Bucket() for i in range(self.range)]        

    def _hash(self, key):
        return key % self.range
    
    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketarray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketarray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucketarray[bucketIndex].exist(key)


class Node:
    def __init__(self, value = 0, nextNode = None) -> None:
        self.value = value
        self.next = nextNode
        

class Bucket:
    def __init__(self) -> None:
        self.head = Node()
    
    def insert(self, value):
        if not self.exist(value):
            newnode = Node(value, self.head.next)
            self.head.next = newnode
        
    def delete(self, value):
        if not self.exist(value):
            print('no such value')
            return None
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return None
            prev = curr
            curr = curr.next

    def exist(self, value):
        curr = self.head.next
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False
        


# hash set implemented by binary search tree

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyrange = 769
        self.bucketarray = [Bucket() for i in range(self.keyrange)]
    
    def _hash(self, key):
        return key % self.keyrange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketarray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketarray[bucketIndex].delete(key)               

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucketarray[bucketIndex].exist(key)

class Bucket:
    def __init__(self) -> None:
        self.tree = BSTree()
    
    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)
    
    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)
    
    def exist(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)
    

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self) -> None:
        self.root = None
        
    def searchBST(self, root: TreeNode, val):
        if not root or root.value == val:
            return root
        
        return self.searchBST(root.left, val) if val < root.value \
            else self.searchBST(root.right, val)
            
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.value:
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.value:
            return root
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
    
    def successor(self, root):
        
        root = root.right
        
        while root.left:
            root = root.left
        return root.value
    
    def predecessor(self, root):
        
        root = root.left
        
        while root.right:
            root = root.right
        
        return root.value
    
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key > root.value:    
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.value:
            root.left = self.deleteNode(root.left, key)
            
        else:
            if not (root.left or root.right):
                root = None
            
            elif root.right:
                root.value = self.successor(root)
                root.right = self.deleteNode(root.right, root.value)
            else:
                root.value = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.value)
                
        return root
        
        
# hash map with array

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]
    
    def _hash(self, key):
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self._hash(key)
        self.hash_table[hash_key].update(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self._hash(key)
        return self.hash_table[hash_key].get(key)
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self._hash(key)
        self.hash_table[hash_key].remove(key)
        

class Bucket:
    def __init__(self):
        self.bucket = []
        
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
            
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

        
        