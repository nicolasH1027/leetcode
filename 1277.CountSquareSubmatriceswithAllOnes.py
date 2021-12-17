class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [0]*(n + 1)
        nums = prev = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]:
                    tmp = dp[j]
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    prev = tmp
                    nums += dp[j]
                else:
                    dp[j] = 0

        return nums