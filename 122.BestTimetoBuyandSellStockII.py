class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0]*2]*(n+1)
        
        dp[0][1] = -float('inf')
        
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i][0] - prices[i-1])
        
        return dp[n][0]
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        profit_0 = 0
        profit_1 = -float('inf')
        
        for i in range(1, n+1):
            profit_0 = max(profit_0, profit_1 + prices[i-1])
            profit_1 = max(profit_1, profit_0 - prices[i-1])
        
        return profit_0
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                ans += prices[i] - prices[i-1]
                
        return ans