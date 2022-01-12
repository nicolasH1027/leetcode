class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        """
        i, j 是 s1 和 s2 的位置， d 是需要字符串的差值
        例如，
        ‘a123’， ‘b32’
        其中一种可能性就是 s1 需要123个字符串， s2需要32个字符串，那么差值就是 91 个    
        
        d 大于0， 代表s1 需要更多字母
        d 小于0， 代表s2 需要更多字母    
        """
        
        @lru_cache(None)
        def dfs(i, j, d):
            
            
            if i == n1 and j == n2:
                "遍历完了两个string， 如果d等于0， 说明所有都匹配了, 否则说明没有匹配"
                return d == 0
        
            elif i < n1 and s1[i].isdigit():
                """
                如果 s1 对应第 i 个位置是数字， 那么我们首先需要遍历s1，直到遍历
                所有的数字字符串，如上例，“a123”， 所有字符串就是 123
                但是， 因为“123”， 有可能是由 “123” 或 “1”， “23” 或  “1”， “2”, "3" 或 “12”， “3” 这几种可能构成，
                所以我们得遍历其中所有可能
                """
                EndPoint = i
                
                while EndPoint < n1 and s1[EndPoint].isdigit(): 
                    "找到所有数字字符串"
                    EndPoint += 1
                    
                
                for pt in range(i+1, EndPoint + 1):
                    "遍历我们刚刚说的所有可能性"
                    if dfs(pt, j, d - int(s1[i:pt])):
                        return True

            elif j < n2 and s2[j].isdigit():
                "同样的操作， 只是从i变成j"
                EndPoint = j
                
                while EndPoint < n2 and s2[EndPoint].isdigit(): 
                    EndPoint += 1
                
                for pt in range(j+1, EndPoint + 1):
                    if dfs(i, pt, d + int(s2[j:pt])):
                        return True  
                    
            elif d == 0 and i < n1 and j < n2 and s1[i] == s2[j]:
                "如果d是0， 那么说明我们之前都匹配了， 只要s1 和 s2 对应i， j位置上的字符相等，我们就进入下一个递归"
                return dfs(i+1, j+1, d)
            
            elif d > 0 and i < n1 and s1[i].isalpha():
                "d > 0 说明 s1 需要更多字母，那么i前进1位， j不动"
                return dfs(i+1, j, d-1)
            
            elif d < 0 and j < n2 and s2[j].isalpha():
                "d < 0 说明 s2 需要更多字母，那么j前进1位， i不动"
                return dfs(i, j+1, d+1)
            
            "所有可能性都无法满足，那么返回false"
            return False
        
        return dfs(0, 0, 0)