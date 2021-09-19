class TrieNode:
    def __init__(self, char = "", value = 0) -> None:
        self.char = char
        self.child = {}
        self.val = value
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        "O(K)"
        cur = self.root
        for cha in key:
            if cha not in cur.child:
                cur.child[cha] = TrieNode(cha)
            cur = cur.child[cha]
        cur.val = val

    def sum(self, prefix: str) -> int:
        "O(m), m is the number of words with the same prefix, dont know how to analyze this "
        def helper(root):
            if not root:
                return
            self.total += root.val
            for node in root.child.keys():
                helper(root.child[node])
        
        cur = self.root
        for cha in prefix:
            if cha not in cur.child:
                return 0
            cur = cur.child[cha]
        
        self.total = 0
        helper(cur)
        return self.total



class TrieNode(object):
    "OG Method, with O(K) for both insertion and sum"
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score



class MapSum(object):

    def __init__(self): 
        self.d = {}

    def insert(self, key, val): 
        "O(1)"
        self.d[key] = val

    def sum(self, prefix):
        "N*k"
        return sum(self.d[i] for i in self.d if i.startswith(prefix))





# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)