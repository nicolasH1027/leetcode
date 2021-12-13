class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        
        upper, lower, left, right = 0, n-1, 0, n-1
        
        ans = [[0]*n for _ in range(n)]
        i = 1
        
        while i <= n*n:
            
            if upper <= lower:
                
                for j in range(left, right + 1):
                    
                    ans[upper][j] = i
                    i += 1
                upper += 1
                
            if left <= right:
                
                for j in range(upper, lower + 1):
                    
                    ans[j][right] = i
                    i += 1
                    
                right -= 1
                
            if upper <= lower:
                
                for j in range(right, left - 1, -1):
                    
                    ans[lower][j] = i
                    i += 1
                    
                lower -= 1
                
            if left <= right:
                
                for j in range(lower, upper - 1, -1):
                    
                    ans[j][left] = i
                    i += 1
                    
                left += 1
        
        return ans
                    
                    