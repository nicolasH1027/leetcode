class TrieNode:
    def __init__(self, char = "") -> None:
        self.char = char
        self.child = {}
        self.count = 0
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, key):
        cur = self.root
        for cha in key:
            if cha not in cur.child:
                cur.child[cha] = TrieNode()
            cur = cur.child[cha]
        cur.count += 1
    
    def search(self, prefix):
        result = ""
        cur = self.root
        for key in prefix:
            if key in cur.child:
                result += key
                cur = cur.child[key]
                if cur.count > 0:
                    break
            else:
                break
        return result if cur.count > 0 else prefix
                

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        tree = Trie()
        for item in dictionary:
            tree.insert(item)
        ls = sentence.split()
        result = []
        for word in ls:
            result.append(tree.search(word))
        
        return " ".join(result)