class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        if stones[1] - stones[0] > 1:
            return False
        
        n = len(stones)
        
        valid = set(stones)
        
        
        @lru_cache(None)
        def helper(i, step):
            if i == stones[-1]:
                return True
            
            if i + step + 1 in valid:
                if helper(i + step + 1, step + 1):
                    return True
            
            if i + step in valid:
                if helper(i + step, step):
                    return True
            
            if step - 1 > 0 and i + step - 1 in valid:
                if helper(i + step - 1, step - 1):
                    return True
            
            return False
        
        return helper(stones[1], stones[1] - stones[0])
    

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        """
        dp[i][k] 意义是
        
        能否到达编号为 i， 且上一次弹跳距离为k。
        
        dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        
        k = stone[i] - stone[j]
        
        优化条件
        
        1.「现在所处的石子编号」为 i 时，「上一次跳跃距离」k 必定满足 k 小于 i
        注意，这里比较的是跳跃距离，不是石头本身代表的位置。
        每次跳动，i都加1， 而跳跃距离最多加一。
        
        2. 当第 i 个石子与第 i-1 个石子距离超过 i 时，青蛙必定无法到达终点
        
        由结论1可以得出结论2
        """
        
        n = len(stones)

        for i in range(1, n):
            if stones[i] - stones[i-1] > i:
                return False
        
        dp = [[False]*n for _ in range(n)]
        
        dp[0][0] = True
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
                if i == n - 1 and dp[i][k]:
                    return True
        
        return False