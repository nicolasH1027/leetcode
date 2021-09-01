class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        length = 0
        start = 0
        
        for i in range(n):
            cur = max(self.getlen(s, i, i, n), self.getlen(s, i, i+1, n))
            if cur < length: continue
            length = cur
            start = i - (cur - 1)//2
        
        return s[start:start+length]
            
        
        
        
    def getlen(self, s, i, j, n):
        
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        
        return j - i - 1
        