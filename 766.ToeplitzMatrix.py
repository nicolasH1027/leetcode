class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
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