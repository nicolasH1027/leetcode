class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        arr = [0]*len(grid)
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                j -=1
            arr[i] = n - j - 1
            
        cnt = 0
        for i in range(n):
            j = i
            num_zero = n - i - 1
            while j < n and arr[i] < num_zero:
                j += 1
            if j == n: return -1
            while j > i:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
                cnt += 1
                
        return cnt
            