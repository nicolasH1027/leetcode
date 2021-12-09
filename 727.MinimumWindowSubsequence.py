class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        m, n, ans = len(s1), len(s2), (float('inf'), 0, 0)
        
        
        "dp[i][j] is defined as the start index that the first i eles in s1 containing first j eles in s2"
        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        """
        dp[i][1], if s1[i] == s2[1], then dp[i][j] == dp[i-1][j-1] which is dp[i-1][0], so it should be i, cause the ith eles in s1 equals to the first element in s2.
        """
        for i in range(m+1):
            dp[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, min(i+1, n+1)):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = dp[i-1][j]

        for i in range(1, m+1):
            if dp[i][n] != -1:
                lenth = i - dp[i][n]
                if lenth < ans[0]:
                    ans = lenth, dp[i][n], i
        
        return s1[ans[1]:ans[2]] if ans[0] != float('inf') else ''
    
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        pt1, pt2, ans = 0, 0, (float('inf'), 0, 0)
        
        while pt1 < len(s1):
            
            if s1[pt1] == s2[pt2]:
                
                if pt2 == len(s2) - 1:
                    
                    end = pt1
                    
                    while pt2 >= 0:
                        while s1[pt1] != s2[pt2]:
                            pt1 -= 1
                        pt1 -= 1
                        pt2 -= 1
                
                    if end - pt1 < ans[0]:
                        ans =  end - pt1, pt1 + 1, end + 1
                else:
                    pt2 += 1
            pt1 += 1
        
        return s1[ans[1]:ans[2]]                    
                         
        
        
