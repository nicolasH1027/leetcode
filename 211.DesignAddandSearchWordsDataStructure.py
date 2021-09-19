class TrieNode:
    def __init__(self, char = "") -> None:
        self.char = char
        self.child = {}
        self.count = 0

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.child:
                cur.child[char] = TrieNode(char)
            cur = cur.child[char]
        cur.count += 1

    
    def search(self, word: str) -> bool:
        
        def helper(word, root):
            if not word:
                return True if root.count > 0 else False
            cha = word[0]
            
            if cha != '.':
                if cha not in root.child:
                    return False
                return helper(word[1:],  root.child[cha])
            
            else:
                for node in root.child:
                    if helper(word[1:], root.child[node]):
                        return True
                return False
        return helper(word, self.root)   
