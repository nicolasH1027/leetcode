"""
此类问题主要有两类，

一类是由kmp以及其各种变种方法构成的，主要是查找匹配字段在原子段是否出现，出现多少次，或者查找公共前缀等问题。

二类则是由 正则表达式 构成的字符串匹配，此类问题一般需要使用动态规划。 先从第二类问题开始
"""


"10. Regular Expression Matching"



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        """
        此题的匹配字段包含 . 和*， 前者匹配一个字符，
        后者则可以匹配0个或者多个前字符，如 a*， 可以匹配
        0个a，或者多个a
        
        通常这种两个字符串组成的问题，一般都dp方向入手。
        dp[i][j] 意思是 s 前i个字符 与 p 前j个字符串是否匹配
        
        根据定义，我们可以尝试写出转移方程，这里，我们需要注意的就是
        *的处理，因为它可以匹配0到多个前字符串
        
        首先定义边界条件， 除了两边都是 "" 空集 的情况， 其余任意一个为0，其状态
        都是False
        
        然后是转移方程，
        
        如果 p[j-1]， 不是 *，
        那么很简单， dp[i][j] = dp[i][j-1] and s[i-1] == p[j-1]
        
        如果 p[j-1] 是 *，
        
        那么我们需要分别讨论几个情况，
        
        如果 s 中 i字符 和 p 中j-1 字符不匹配怎么办， 那么dp[i][j]的状态由dp[i][j-2]的状态决定，因为*可以表示0个
        dp[i][j] = dp[i][j-2]
        
        
        https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/
        以一个例子详解动态规划转移方程：
        S = abbbbc
        P = ab*d*c
        1. 当 i, j 指向的字符均为字母（或 '.' 可以看成一个特殊的字母）时，
        只需判断对应位置的字符即可，
        若相等，只需判断 i,j 之前的字符串是否匹配即可，转化为子问题 f[i-1][j-1].
        若不等，则当前的 i,j 肯定不能匹配，为 false.
        
            f[i-1][j-1]   i
                    |        |
        S [a  b  b  b  b][c] 
        
        P [a  b  *  d  *][c]
                            |
                            j
        

        2. 如果当前 j 指向的字符为 '*'，则不妨把类似 'a*', 'b*' 等的当成整体看待。
        看下面的例子

                    i
                    |
        S  a  b [b] b  b  c  
        
        P  a [b  *] d  *  c
                    |
                    j
        
        注意到当 'b*' 匹配完 'b' 之后，它仍然可以继续发挥作用。
        因此可以只把 i 前移一位，而不丢弃 'b*', 转化为子问题 f[i-1][j]:
        
                i
                | <--
        S  a [b] b  b  b  c  
        
        P  a [b  *] d  *  c
                    |
                    j
        
        另外，也可以选择让 'b*' 不再进行匹配，把 'b*' 丢弃。
        转化为子问题 f[i][j-2]:

                    i
                    |
        S  a  b [b] b  b  c  
            
        P [a] b  *  d  *  c
            |
            j <--

        3. 冗余的状态转移不会影响答案，
        因为当 j 指向 'b*' 中的 'b' 时, 这个状态对于答案是没有用的,
        原因参见评论区 稳中求胜 的解释, 当 j 指向 '*' 时,
        dp[i][j]只与dp[i][j-2]有关, 跳过了 dp[i][j-1].
                
        
        
        """
        
        m, n = len(s), len(p)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        def match(i, j):
            if i == 0:
                return False
            elif p[j-1] == '.':
                return True
            else:
                return s[i-1] == p[j-1]
        
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if match(i, j-1):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and match(i, j)
                    
        return dp[m][n]
        