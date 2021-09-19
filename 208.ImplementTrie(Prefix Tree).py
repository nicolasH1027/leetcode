class TrieNode:
    def __init__(self, char = "") -> None:
        self.char = char
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for cha in word:
            if cha not in cur.child:
                cur.child[cha] = TrieNode(cha)
            cur = cur.child[cha]
        cur.count += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for cha in word:
            if cha not in cur.child:
                return False
            cur = cur.child[cha]
        
        return True if cur.count >= 1 else False
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for cha in prefix:
            if cha not in cur.child:
                return False
            cur = cur.child[cha]
        return True