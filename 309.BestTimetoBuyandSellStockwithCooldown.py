class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [[0]*2 for _ in range(n+1)]
        
        dp[0][1] = -float('inf')
        
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[0])
        dp[1][1] = max(dp[0][1], - prices[0])
        
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
        
        return dp[n][0]
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        profit0 = lag2profit0 = 0
        profit1 = -float('inf')
        
        for i in range(1, n+1):
            nextprofit0 = max(profit0, profit1 + prices[i-1])
            nextprofit1 = max(profit1, lag2profit0 - prices[i-1])
            lag2profit0 = profit0
            profit0 = nextprofit0
            profit1 = nextprofit1
            
        return profit0