class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        It's a typical backtrack problem, I dont know why the OG offers the DP solution,
        also, it can be solved by trie tree
        """
        result = []
        def backtrack(s, wordDict, start, track):
            if start == len(s):
                result.append(' '.join(track))
                return 
            
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordDict:
                    track.append(s[start : end])
                    backtrack(s, wordDict, end, track)
                    track.pop()
        
        backtrack(s, frozenset(wordDict), 0, [])
        return result
                    
                    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        With memorization
        For trie solution, the code would be so lengthy,
        maybe it woule a little bit more efficient, but
        it too difficult to finish it in the interview
        """
        result = []
        @lru_cache
        def backtrack(s, wordDict, start, track):
            if start == len(s):
                result.append(track[:-1])
                return 
            
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordDict:

                    backtrack(s, wordDict, end, track + s[start : end] + " ")
        
        backtrack(s, frozenset(wordDict), 0, "")
        return result
    

