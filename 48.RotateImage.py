class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Ori      Tranpose    mirror on  y
        1 2 3    1 4 7     7 4 1
        4 5 6    2 5 8     8 5 2
        7 8 9    3 6 9     9 6 3
        """
        # transpose 
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # mirror
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 -j] = matrix[i][n - 1 -j], matrix[i][j] 
                
        # or we can use the builtin function 
        # for i in range(n):
        #     matrix[i].reverse()

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate four cells 
        1 2 3     3   3 2 1     7 2 1    7 2 1   3 2 1
        4 5 6         4 5 6     4 5 6    4 5 6   4 5 6
        7 8 9         7 8 9     3 8 9    9 8 3   9 8 3
        
        """

        n = len(matrix[0])
        for i in range(n // 2 ):
            for j in range(i, n - 1 - i):
                tmp = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = matrix[j][i]
                matrix[j][i] = matrix[n - 1 - i][j]
                matrix[n - 1 - i][j] = matrix[n - 1 - j][n - 1 - i]
                matrix[n - 1 - j][n - 1 - i] = tmp
        

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        for i in range(n):
            for j in range(0, n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i -1], matrix[i][j]
                

        # mirror on x 
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]