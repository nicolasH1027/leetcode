class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def backtrack(numSum, i):
            if i == len(nums):
                if numSum == target:
                    return 1
                else:
                    return 0
            
            result = 0
            for op in [-1, 1]:
                numSum += op*nums[i]
                result += backtrack(numSum, i+1)
                numSum -= op*nums[i]
            return result 
        
        return backtrack(0, 0)
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        "DP solution"
        
        
        if sum(nums) < abs(target) or (target + sum(nums)) % 2 == 1:
            return 0
        
        m, n = len(nums),  (target + sum(nums)) // 2
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(m+1):
            dp[i][0] = 1
            
        
        for i in range(1, m + 1):
            for j in range(n + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[m][n]
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        "DP solution"
        
        
        if sum(nums) < abs(target) or (target + sum(nums)) % 2 == 1:
            return 0
        
        m, n = len(nums),  (target + sum(nums)) // 2
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(m+1):
            dp[i][0] = 1
            
        
        for i in range(1, m + 1):
            for j in range(n + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[m][n]
    

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        "DP solution"
        
        
        if sum(nums) < abs(target) or (target + sum(nums)) % 2 == 1:
            return 0
        
        m, n = len(nums),  (target + sum(nums)) // 2
        
        dp = [0]*(n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(n, -1, -1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] + dp[j - nums[i-1]]
                else:
                    dp[j] = dp[j]
                    
        return dp[n]