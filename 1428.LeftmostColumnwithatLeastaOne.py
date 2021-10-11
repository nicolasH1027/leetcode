# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        O(MlogN)
        """
        m, n = binaryMatrix.dimensions()
        
        def binarysearch(row, lo, hi):
            while lo < hi:
                mid = lo + (hi - lo)//2

                if binaryMatrix.get(row, mid) < 1:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        k = inf
        lo, hi = 0, n - 1
        for i in range(m):
            
            if binaryMatrix.get(i, hi) == 0:
                continue
            hi = binarysearch(i, lo, hi)
            k = min(k, hi)
        return k if k != inf else -1
            
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        """
        O(M + N)
        """
        
        rows, cols = binaryMatrix.dimensions()
        
        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1
        
        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1
        
        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1
            
            
        
        
        
        

        
            