class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        n = len(s)
        
        dp = [0]*(n+1)
        
        