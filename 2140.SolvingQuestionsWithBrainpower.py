class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        """
        对于每一个question， 我们只需要考虑做与不做，其实就是01背包问题
        """
        
        n = len(questions)
        
        @lru_cache(None)
        def dfs(ind):
            
            if ind > n - 1:
                return 0
            
            return max(dfs(ind+1), questions[ind][0] + dfs(ind + questions[ind][1] + 1))
        
        return dfs(0)
    

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        
        dp = [0]*(n+1)
        
        """
        dp 三部曲
        
        1. 定义
        dp[i] 的定义是 从i开始的最大score， 这里注意，从i开始不代表一定要选i
        
        2.转移方程
        dp[i] = max(questions[i][0] + dp[i + questions[i][1] + 1], dp[i+1])
        
        3.边界条件
        
        dp[n] = 0, 因为计算i的时候需要计算i+1和其它dp值，所以我们从右往左扫
        """
        
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
        
        return dp[0]
        