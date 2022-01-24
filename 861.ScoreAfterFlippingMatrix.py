class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        """
        贪心想法
        
        最高位开始，把所有0换成1
        
        然后从第二列开始，统计0和1的数量，然后换成最多的1
        
        注意的是，对于首位不是1的行，我们要进行反转，因为一开始反转了
        """
        
        m, n = len(grid), len(grid[0])
        
        ans = m * (1 << (n - 1))
        
        for j in range(1, n):
            
            num_one = 0
            
            for i in range(m):
                
                if grid[i][0]:
                    
                    num_one += grid[i][j]
                
                else:
                    
                    num_one += 1 - grid[i][j]
            
            k = max(num_one, m - num_one)
            
            ans += k * (1 << (n - j - 1))
        
        return ans
