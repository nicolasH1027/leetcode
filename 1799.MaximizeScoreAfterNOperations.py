class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        """
        top down
        
        dp(mask)
        
        首先 mask 是一个二进制数， 如， 11111，第i位是1，那么代表nums里面第i位已经被使用了
        所以，dp(mask)代表已经使用了mask中的元素的最大值
        
        所以，根据 trasnlation relationship 就是
        枚举每一对可能的组合，然后选最大的
        dp(mask) = max(dp(mask),  op*gcd(nums[i], nums[j]) + dp(    mask | (1 << i) | (1 << j)     ))
        
        """
        
        @lru_cache(None)
        def gcd(x, y):
            return math.gcd(x, y)
        
        @lru_cache(None)
        def dp(mask):
            if mask == fullstate:
                return 0
            ans = 0
            op = bin(mask).count('1')//2 + 1
            for i in range(n):
                for j in range(i+1, n):
                    if not mask & (1 << i) and not mask & (1 << j): 
                        ans = max(ans, op*gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j)))
            return ans
        
        n = len(nums)
        fullstate = 1 << n - 1
        
        return dp(0)
    

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        """
        bottom up
        """
        @lru_cache(None)
        def gcd(x,y):
            return math.gcd(x, y)
        
        n = len(nums)
        dp = [0]*(1 << n)
        
        for mask in range(1 << n):
            cnt = bin(mask).count('1')
            if cnt & 1: continue
            op = cnt//2 + 1
            for i in range(n):
                for j in range(i + 1, n):
                    if (mask & (1 << i)) + (mask & (1 << j)) == 0:
                        nxt_mask = mask | (1 << i) | (1 << j)
                        dp[nxt_mask] = max(dp[nxt_mask], op*gcd(nums[i], nums[j]) + dp[mask])
        print(dp)
        return dp[-1]