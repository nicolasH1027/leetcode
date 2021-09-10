class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def backtrack(left, right, s):
            
            if len(s) == 2*n:
                result.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(left + 1, right, s)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(left, right + 1, s)
                s.pop()
        
        backtrack(0, 0, [])
        return result
            
            
        
        