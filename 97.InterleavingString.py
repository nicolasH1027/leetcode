class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        dp[0][0] = 1
        
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for i in range(1, n2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n1][n2]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        if n1 < n2:
            return self.isInterleave(s2, s1, s3)
        
        dp = [0]*(n2+1)
        dp[0] = 1
        
        for i in range(1,n2+1):
            dp[i] = dp[i-1] and s2[i-1] == s3[i-1]
        
        prev = 1
        
        for i in range(1, n1+1):
            prev = prev and s1[i-1] == s3[i-1]
            dp[0] = prev
            for j in range(1, n2+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1]) 
                
        return dp[n2] 