class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        "very slow"
        m, n, seen = len(obstacleGrid), len(obstacleGrid[0]), set([0,0])
        
        def valid(x, y):
            if 0 <= x < m and 0 <= y < n and obstacleGrid[x][y] != 1 and (x, y) not in seen:
                return True
            else:
                return False
            
        if not valid(0,0) or not valid(m-1,n-1):
            return 0
        
        @lru_cache(None)
        def backtracking(x, y):
            
            if x == m - 1 and y == n - 1:
                return 1
            
            ans = 0
            
            for dx, dy in [[1,0], [0,1]]:
                nx, ny = x+dx, y+dy
                if valid(nx, ny):
                    seen.add((nx,ny))
                    ans += backtracking(nx, ny)
                    seen.remove((nx,ny))
            
            return ans
        
        
        return backtracking(0, 0)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        """
        dp[i][j] is defined as the number of path that we can reach i, j
        """
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        
        """
        因为我们每次都是从 上面和左边进行累加的，那么对于原数组的 0,0 位置上的数字
        我们需要加上面或者是左边的padding上的某个设置成1,那么如果0,0上的位置合法，我们
        就可以直接加上去，就等于一，不需要再特别去设置了
        """
        dp[0][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]
    
    
    
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0]*(n+1)

        dp[0] = 1 
        
        for i in range(1, m+1):
            
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] != 1:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
                    
            dp[0] = 0 #主要是这一步，需要我们每次重新把第一值重新设着成0
            
        return dp[n]