class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if k >= n//2:
            ans = 0
            for i in range(1, n):
                if prices[i] - prices[i-1] > 0:
                    ans += prices[i] - prices[i-1]
                    
            return ans
        else:
            dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]
            
            for i in range(k+1):
                dp[0][i][1] = -float('inf')
            
            for i in range(1, n+1):
                for j in range(k, 0, -1):
                    "注意这里需从大到小更新，dp[i][j][1] 需要用到 dp[i-1][j-1][0]的值"
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i-1])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i-1])
            
            return dp[n][k][0]
        

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if k >= n//2:
            ans = 0
            for i in range(1, n):
                if prices[i] - prices[i-1] > 0:
                    ans += prices[i] - prices[i-1]
                    
            return ans
        else:
            dp = [[0]*2 for _ in range(k+1)]
            
            for i in range(k+1):
                dp[i][1] = -float('inf')
            
            for i in range(1, n+1):
                for j in range(k, 0, -1):
                    "注意这里需从大到小更新，dp[j][1] 需要用到 dp[j-1][0]的值"
                    dp[j][0] = max(dp[j][0], dp[j][1] + prices[i-1])
                    dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i-1])
            
            return dp[k][0]
        