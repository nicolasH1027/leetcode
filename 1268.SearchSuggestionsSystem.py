class Trie:
    def __init__(self):
        self.child = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        def insert(root, word):
            node = root
            for c in word:
                node = node.child.setdefault(c, Trie())
                node.suggestions.append(word)
                node.suggestions.sort()
                if len(node.suggestions) > 3:
                    node.suggestions.pop()
        
        root = Trie()
        
        for product in products:
            node = root
            insert(node, product)
            
        ans = [[] for _ in range(len(products))]
        
        node = root
        for i, ch in enumerate(searchWord):
            if ch in node.child:
                ans[i] = node.child[ch].suggestions[:]
                node = node.child[ch]
            else:
                break
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        ans, prefix, i = [], "", 0
        
        for word in searchWord:
            prefix += word
            i = bisect.bisect_left(products, prefix, i)
            ans.append([w for w in products[i:i+3] if w.startswith(prefix)])
            
        return ans