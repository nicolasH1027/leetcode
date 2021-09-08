class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        "binary search"
        m = len(matrix) 
        n = len(matrix[0])
        
        for i in range(min(m, n)):
            if self.binarysearch(matrix, i, m-1, n-1, target, horizontal = True) or self.binarysearch(matrix, i, m-1, n-1, target, horizontal = False):
                return True
        return False
    
    def binarysearch(self, matrix, start, mrow, ncol, target, horizontal = True):  
        if horizontal:
            left = start
            right = ncol
            while left <= right:
                mid = left + (right - left)//2
                if matrix[start][mid] == target:
                    return True
                elif  matrix[start][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            up = start
            bot = mrow
            while up <= bot:
                mid = up + (bot - up)//2
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] < target:
                    up = mid + 1
                else:
                    bot = mid - 1
        return False
            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        "divide and conquer"
        if not matrix:
            return False
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        bottom = len(matrix) - 1
        return self.divideandconquer(matrix, target, left, right, up, bottom)
    
    def divideandconquer(self, matrix, target, left, right, up, bottom):
        if left > right or up > bottom:
            return False
        if matrix[up][left] > target or matrix[bottom][right] < target:
            return False
        pivot = left + (right - left)//2
        row = up
        while row <= bottom and matrix[row][pivot] <= target:
            if matrix[row][pivot] == target:
                return True
            row += 1 
        return self.divideandconquer(matrix, target, left, pivot-1, row, bottom) \
            or self.divideandconquer(matrix, target, pivot + 1, right, up, row - 1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        "tricky way"
        "we can start from bottom left or top right"
        
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        
        while left <= right and bottom >= up:
            if matrix[bottom][left] == target:
                return True
            elif matrix[bottom][left] < target:
                left += 1
            else:
                bottom -= 1
        return False 
        
        
        