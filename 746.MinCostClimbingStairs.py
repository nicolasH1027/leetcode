class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        fir = sec = 0
        
        ans = float('inf')
        
        for i in range(2, n+1):
            ans = min(fir + cost[i-1], sec + cost[i-2])
            sec = fir
            fir = ans
        
        return ans