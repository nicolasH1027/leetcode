class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [[[0]*2 for _ in range(3)] for _ in range(n+1)]
        
        for i in range(3):
            dp[0][i][1] = -float('inf')
            
        for i in range(1, n+1):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])
            
        return dp[n][k][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        profit_10 = 0
        profit_11 = -float('inf')
        
        profit_20 = 0
        profit_21 = -float('inf')
        
            
        for i in range(1, n+1):
            "注意这里的update顺序是有影响的"
            profit_20 = max(profit_20, profit_21 + prices[i-1])
            profit_21 = max(profit_21, profit_10 - prices[i-1])
            profit_10 = max(profit_10, profit_11 + prices[i-1])
            profit_11 = max(profit_11, -prices[i-1])
            
        return profit_20