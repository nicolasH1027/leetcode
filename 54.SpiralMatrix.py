class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n, i = len(matrix), len(matrix[0]), 0
        
        upper, lower, left, right = 0, m-1, 0, n-1
        
        ans = []
        
        while len(ans) < m*n:
            
            if upper <= lower:
                
                for j in range(left, right + 1):
                    
                    ans.append(matrix[upper][j])
                
                upper += 1
                
            if left <= right:

                for j in range(upper, lower + 1):

                    ans.append(matrix[j][right])
                    
                right -= 1
                
            if upper <= lower:
                
                for j in range(right, left - 1, -1):
                    
                    ans.append(matrix[lower][j])
                    
                lower -= 1
                
            if left <= right:
                
                for j in range(lower, upper - 1, -1):
                    
                    ans.append(matrix[j][left])
                    
                left += 1
                
        return ans