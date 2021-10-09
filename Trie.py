class TrieNode:
    def __init__(self, char = "") -> None:
        self.char = char
        self.child = {}
        self.count = 0
        # self.first = -1

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        # self.time = 0
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # self.time += 1
        cur = self.root
        for cha in word:
            if cha not in cur.child:
                cur.child[cha] = TrieNode(cha)
            cur = cur.child[cha]
        cur.count += 1
        # if cur.count:
        #     cur.first = self.time

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
    
    def remove(self, word:str):
        """
        the function will remove word regardless how many times it appear.
        """
        def helper(node, word, level):
            if level == len(word):
                return len(node.child) == 0
            if word[level] not in node.child:
                return False
            
            if helper(node[word[level]], word, level + 1):
                node.child.pop(word[level])
                return len(node.children) == 0 and node.count == 0
            return False
        helper(word)

      
            
            


# Handy way to build the Trie 

# WORD_KEY = '$'

# trie = {}
# for word in words:
#     node = trie
#     for letter in word:
#         node = node.setdefault(letter, {})
#     node[WORD_KEY] = word
    
    
    
end = 'end'

tire = {}

for word in words:
    node = tire
    for letter in word:
        node = node.setdefault(letter, {})
    node[end] = end
    
node = tire
for letter in prefix:
    if letter not in node:
        return False
    node = tire[letter]
return end in node