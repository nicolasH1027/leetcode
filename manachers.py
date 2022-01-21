

"""
马拉车算法实现

其实可以算是kmp的拓展，认真看代码的话，其实和 Z algorithm 非常像
"""

def manachers(s: str):
    
    "expand the original string"
    
    A = '@#' + '#'.join(s) + '#$'
    Z = [0] * len(A)
    
    """
    Z 用来保存每个点可以由中心向左右拓展的次数
    
    其中， 找到最大的Z[i], 然后(i - Z[i])//2 就是最长回文子串的起始点
    
    s[(i - Z[i])//2, Z[i]] 这个就是最长回文子串
    """
    
    center = right = 0
    
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
            
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
            
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z



def Z_algorithm(s):
    
    "这个是z算法，用来解决公共前序问题"
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return n + sum(z)