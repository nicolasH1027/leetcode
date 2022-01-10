class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        dp[i][k][j] 在第i天最多进行k次交易且持有状态为j的最大收益
        
        j in [0, 1]
                
        https://leetcode-cn.com/circle/article/qiAgHn/
        """
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][1] = -float('inf')
        
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], -prices[i-1])
        
        return dp[n][0]
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit_0 = 0
        profit_1 = -float('inf')
        for i in range(1, n+1):
            profit_0 = max(profit_0, profit_1 + prices[i-1])
            profit_1 = max(profit_1, -prices[i-1])
        
        return profit_0