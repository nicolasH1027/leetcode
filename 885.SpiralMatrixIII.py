class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        def valid(i, j): 
            return 0 <= i < rows and 0 <= j < cols
        
        n = rows*cols

        r, c = rStart, cStart

        ans, i, step = [[rStart, cStart]], 1, 1
        
        while i < n:
            
            for _ in range(step):
                
                r, c = r, c + 1
                if valid(r, c):
                    ans.append([r, c])
                    i += 1
                    
            for _ in range(step):
                
                r, c = r + 1, c
                if valid(r, c):
                    ans.append([r, c])
                    i += 1
                    
            step += 1
            
            for _ in range(step):
                
                r, c = r, c - 1
                if valid(r, c):
                    ans.append([r, c]) 
                    i += 1
                    
            for _ in range(step):
                
                r, c = r - 1, c
                if valid(r, c):
                    ans.append([r, c])
                    i += 1
            step += 1
        
        return ans