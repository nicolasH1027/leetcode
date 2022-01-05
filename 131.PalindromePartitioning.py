class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        调用lru帮我们处理重复结果
        """
        @lru_cache(None)
        def check(start, end):
            left, right = start, end
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtracking(ind):
            if ind == n:
                ans.append(tmp[:])
                return 
            
            for i in range(ind, n):
                if check(ind, i):
                    tmp.append(s[ind:i+1])
                    backtracking(i+1)
                    tmp.pop()
        
        ans, tmp, n = [], [], len(s)
        
        backtracking(0)
        
        return ans
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        不使用lru，直接预处理，使用dp计算出所有可能性
        """
        
        n = len(s)
        dp = [[True]*n for _ in range(n)]
        
        """
        注意这里的loop的顺序，i得从后面往前
        这样的话，配合内循环，就是不断的从 i, j到
        i-1, j+1扩张。
        如果i从前往后，那么内部子串没有计算就得计算外部
        子串，答案就是错的
        """
        for i in range(n -1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

        def dfs(ind):
            if ind == n:
                ans.append(tmp[:])
                return 
            
            for i in range(ind, n):
                if dp[ind][i]:
                    tmp.append(s[ind:i+1])
                    dfs(i+1)
                    tmp.pop()
                    
        tmp, ans = [], []
        dfs(0)
        return ans