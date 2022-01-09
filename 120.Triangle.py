class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        dp = [[0]*(m+1) for _ in range(m+1)]
        dp[1][1] = triangle[0][0]
        
        for i in range(2, m+1):
            
            for j in range(1, i+1):
                if j == 1:
                    dp[i][1] = dp[i-1][1] + triangle[i-1][0]
                elif j == i:
                    dp[i][i] = dp[i-1][i-1] + triangle[i-1][i-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]
                
        return min(dp[m][1:])
    

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        dp = [0]*(m+1)
        dp[1] = triangle[0][0]
        
        for i in range(2, m+1):
            dp[i] = dp[i-1] + triangle[i-1][i-1]
            for j in range(i-1, 1, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i-1][j-1]
            dp[1] += triangle[i-1][0]
        
        return min(dp[1:])