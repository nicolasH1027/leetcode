class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def is_concated(word):
            n = len(word)
            dp = [0]*(n+1)
            dp[0] = 1
            
            for i in range(n + 1):
                if dp[i]:
                    root = Trie
                    for j in range(i, n):
                        c = word[j]
                        if c not in root: break
                        root = root[c]
                        if '###' in root and root['###'] != word:
                            dp[j + 1] = 1
            return dp[n]

        Trie = {}
        
        for word in words:
            if word:
                node = Trie
                for letter in word:
                    node = node.setdefault(letter, {})
                node['###'] = word

        ans= []
        
        for word in words:
            if word:
                if is_concated(word):
                    ans.append(word)
            
        return ans