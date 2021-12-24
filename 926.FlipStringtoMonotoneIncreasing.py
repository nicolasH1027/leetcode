class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n, cnt = len(s), 0
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            
            if s[i-1] == '1':
                cnt += 1
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+1, cnt)

        return dp[n]
            

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        n, cnt = len(s), 0
        dp = 0
        for i in range(1, n+1):
            
            if s[i-1] == '1':
                cnt += 1
            else:
                dp = min(dp+1, cnt)
        return dp


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        对于每一个 i in [0, n-1]， 我们记录i左边有x个1， 右边有y个0，
        那么对于每个i， 我们则需要转变 x + y 个数， 最后我们求从0到n-1
        的最小操作数
        """
        
        n = len(s)
        cnt = [0]*(n+1)
        
        for i in range(1, n+1):
            cnt[i] = cnt[i-1] + int(s[i-1])

        
        """
        left side, 我们有 cnt[i-1] 个 1，右边总共有 n - i （i从1 到n， 而且
        不包含第i个元素）， cnt[n]总共有多少个1， 减去cnt[i] 
        """
        
        return min(cnt[i-1] + n - i - cnt[n] + cnt[i] for i in range(1, n+1))
            
            
        