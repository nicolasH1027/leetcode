class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        @lru_cache(maxsize = None)
        def backtracking(ind):
            
            if ind == n:
                return 1
            
            ans = 0
            
            for i in range(2):
                
                if s[ind] == '0': break
                if ind + i + 1 > n or int(s[ind: ind + i + 1]) > 26: break
                
                ans += backtracking(ind + i + 1)
            
            return ans
        
        return backtracking(0)
                
                
                
class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        dp[i] = Number of ways of decoding substring of size i
        """
        n = len(s)
        dp =[0]*(n+1)
        
        dp[0] = 1
        dp[1] = (s[0] != '0')*1
        
        for i in range(2, n+1):
            
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
        return dp[n]
        
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        one_lag = (s[0] != '0')*1
        two_lag = 1
        
        
        for i in range(2, n+1):
            ans = 0
            if s[i-1] != '0':
                ans += one_lag
            
            if 10 <= int(s[i-2:i]) <= 26:
                ans += two_lag
            
            two_lag = one_lag
            one_lag = ans
            
        return one_lag
            