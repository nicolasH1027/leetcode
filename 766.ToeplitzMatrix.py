class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        """
        O(row*col) time, O(row + col)
        """
        row = len(matrix)
        col = len(matrix[0])
        
        pos = collections.defaultdict(int)
        
        for i in range(row):
            for j in range(col):
                if i - j not in pos:
                    pos[i - j] = matrix[i][j]
                else:
                    if pos[i - j] != matrix[i][j]:
                        return False
        return True
    
    
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]: 
                    return False
        return True
    
    
"""
For the follow up question
"""

"""
Follow up 1

Each time, we can only store one row
1 2 3 4
5 1 2 3
9 5 1 2

  1 2 3
5 1 2 3 

  5 1 2
9 5 1 2
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])              
        
        expected = collections.deque()
        
        for i in range(n):
            expected.append(matrix[0][i])
            
        for i in range(1, m):
            print('==')
            expected.pop()
            expected.appendleft(matrix[i][0])
            
            for j in range(1, n):
                if matrix[i][j] != expected[j]:
                    return False
            
        return True
    

"""
Follow up 2

Each time, we can only store partial one row
1 2 3 4      1  2     2 3     3  4
5 1 2 3  =   5  1  +  1 2  +  2  3 
9 5 1 2      9  5     5 1     1  2

Divide the original into several submatrix with overlap column
"""