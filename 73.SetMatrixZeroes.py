class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        straight forward solution O(m*n(m+n)) time, O(m*n) space
        """
        seen = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        def mark(i, j):
            if matrix[i][j] == 0:
                for k in range(m):
                    if matrix[k][j] != 0:
                        matrix[k][j] = 0
                        seen.add((k, j))
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] = 0
                        seen.add((i, k))
                        
        for i in range(m):
            for j in range(n):
                if (i, j) in seen: continue
                mark(i, j)
                
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        straight forward solution 
        
        Little improvement,  O(m + n) time, O(m + n) space 
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = set()
        col = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
                    
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        is_col = False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            
            if matrix[i][0] == 0:
                is_col = True
            
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0