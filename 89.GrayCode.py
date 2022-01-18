class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        """
        binary code into gray code
        
        https://blog.csdn.net/jingfengvae/article/details/51691124
        """
        
        ans = [0]*(1 << n)
        
        for i in range(1 << n):
            ans[i] = i ^ (i >> 1)
        
        return ans
    


"""
如何将 gray code 转换成 binary code 呢？
"""

def binary(gray):
    bi = gray
    gray >>= 1
    
    while gray:
        bi ^= gray
        gray >>= 1
        
    return bi