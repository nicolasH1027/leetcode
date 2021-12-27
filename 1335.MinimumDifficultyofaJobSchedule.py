class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        """
        dp[i][j] means the minimum difficulty of the first j day for the first
        i jobs
        
        1,2,3,..............i,

        1 2 3 4 5 6 7 j-1,  j, j+1, j+2, j+3

        ---->>>

        1,2,3,........k,    k+1......i,

        1 2 3 4 5 6 7 j-1,        j,   j+1, j+2, j+3
        
        divide 1-i into two parts, 1:k belongs to first j-1 day,
        k+1:i belongs to jth day

        j - 1 <= k < i
        time: nnd
        space: nd
        """
        
        m = len(jobDifficulty)
        
        if m < d:
            return -1
        
        dp = [[float('inf')]*(d+1) for _ in range(m+1)]
        dp[0][0] = 0
        
        for i in range(1, m+1):
            for j in range(1, d+1):
                tmp = 0
                for k in range(i-1, j-2, -1):
                    tmp = max(tmp, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + tmp)

        return dp[m][d] if dp[m][d] != float('inf') else -1
    

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        time: nnd
        space: n
        """
        n = len(jobDifficulty)
        
        if n < d:
            return -1
        
        dp, max_cur = [0]*(n+1), 0
        for i, val in enumerate(jobDifficulty):
            max_cur = max(max_cur, val)
            dp[i+1] = max_cur
            
        for j in range(1, d+1):
            for i in range(n, 0, -1):
                tmp, cost = 0, float('inf')
                for k in range(i-1, j-2, -1):
                    tmp = max(tmp, jobDifficulty[k])
                    cost = min(cost, dp[k] + tmp)
                dp[i] = cost
                
        return dp[n]
    

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        time: nd
        space: n
        
        不会
        """
        
        
        