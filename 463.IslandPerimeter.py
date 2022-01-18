class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        "直觉做法"
        m, n = len(grid), len(grid[0])

        def count(x, y):
            ans = 4 
            for dx, dy in [[-1,0], [1,0], [0,1], [0,-1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny]:
                        ans -= 1            
            return ans
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += count(i, j)
                    
        return ans
    

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        """
        上面的做法有很多重复计算，例如 i j 是1 了，那么i+1, j还是1的话，其实不用再去
        计算上面的那个了
        
        
        如何简化呢，
        
        假设每次遇到1，我们就加4，然后判断上面是否有1，如果有就减2，
        
        然后判断左边是否有1， 有就减2，
        
        第一行和第一列不用判断，这样就可以简化很多计算
        """
        m, n = len(grid), len(grid[0])
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                
                if not grid[i][j]: continue
                ans += 4
                
                if i and grid[i-1][j]:
                    ans -= 2
                
                if j and grid[i][j-1]:
                    ans -= 2
                    
        return ans
                