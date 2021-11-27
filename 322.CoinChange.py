class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        "much more faster"
        
        @lru_cache(maxsize=None)
        def dp(amount):
            
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            res = float('inf')
            
            for coin in coins:
                sub = dp(amount - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            
            return -1 if res == float('inf') else res
        
        return dp(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        "manually memorization, less efficient"
        
        memo = {}
        
        def dp(amount):
            
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            res = float('inf')
            
            for coin in coins:
                sub = dp(amount - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            
            memo[amount] = -1 if res == float('inf') else res
            
            return -1 if res == float('inf') else res

        return dp(amount)
    

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
        return -1 if dp[amount] == float('inf') else dp[amount]
            