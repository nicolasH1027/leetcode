class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return False
        
        tol = sum(nums)
        mean = tol // 2
        
        if tol % 2 != 0:
            return False
        n = len(nums)
        
        dp = [[0]*(mean + 1) for _ in range(n + 1)]
        
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, mean + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][mean]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return False
        
        tol = sum(nums)
        mean = tol // 2
        
        if tol % 2 != 0:
            return False
        n = len(nums)
        
        dp = [0]*(mean + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(mean, 0, -1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] or dp[j - nums[i-1]]
                else:
                    dp[j] = dp[j]
                    
        return dp[mean]