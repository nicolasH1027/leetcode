class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Naive traverse, backtrack, TLE
        But, does this remind you the Fibonacci number?
        """
        def backtrack(s, word, start):
            """
            O(2^n)
            """
            if start == len(s):
                return True
            for tar in range(start + 1,  len(s) + 1):
                if s[start:tar] in word and backtrack(s, word, tar):
                    return True
            return False
        
        return backtrack(s, wordDict, 0)
            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Yes, in Fibonacci number, we re-compute the number many times, so
        how do we overcome that? 
        cache!
        """
        @lru_cache
        def backtrack(s, word, start):
            """
            """
            if start == len(s):
                return True
            for tar in range(start + 1,  len(s) + 1):
                if s[start:tar] in word and backtrack(s, word, tar):
                    return True
            return False
        return backtrack(s,frozenset(wordDict), 0)
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        BFS, the general idea are the same with above methods
        """
        
        wordDict = set(wordDict)
        queue = collections.deque()
        queue.append(0)
        seen = set()
        
        while queue:
            cur = queue.popleft()
            if cur in seen: continue
            for next in range(cur + 1, len(s) + 1):
                if s[cur:next] in wordDict:
                    if next == len(s):
                        return True
                    queue.append(next)
                seen.add(cur)
        return False



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        DP, the same idea
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        max(n^2, M), M is the number of all the letter in word dict
        """
        Trie, max_len, END, n = {}, 0, 'END', len(s)

        for word in wordDict:
            max_len = max(max_len, len(word))
            node = Trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[END] = END
        
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(n+1):
            if dp[i]:
                root = Trie
                for j in range(i, n):
                    c = s[j]
                    if j - i + 1 > max_len or c not in root:
                        break
                    root = root[c]
                    if END in root:
                        dp[j+1] = 1
        
        return dp[n]
                
        
        
        
            
        