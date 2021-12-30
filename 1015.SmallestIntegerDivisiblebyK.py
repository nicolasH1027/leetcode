class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        首先排除 k % 2 == 0， 因为奇数无法被偶数整除.
        其次， 如果k % 5 == 0, 也可以被排除，因为如果被5
        整除，最后一位只能是0或者5
        
        其次，正常我们是用 x*10 + 1去测试下一数能否被整除。
        
        111 % 17 = (6 * 17 + 9) % 17 = 9
        
        （111 * 10 + 1）% k = 1111 % k
        
        == (（6 * 17 + 9）*10 + 1) % k
        
        == (9*10 + 1) % k 
        
        所以 与其用 x * 10 + 1 作为下一个数，我们可以
        
        (x % k) * 10 + 1 作为下一个数
        
        最后
        
        Now, the only problem is how to check whether the required number N exists.
        Notice that if N does not exist, this while-loop will continue endlessly. 
        However, the possible values of remainder are limited -- ranging from 0 to K-1. 
        Therefore, if the while-loop continues forever, the remainder repeats. 
        Also, if remainder repeats, then it gets into a loop. Hence, the while-loop is endless if and only if the remainder repeats.
        
        总共就 k 个不同的余数，循环 k 次之后，如果还没有出现0， 那么意味着别的余数出现了大于2的次数，那么意味着出现了循环
        
        Recall that the number of possible values of remainder (ranging from 0 to K-1) is limited, 
        and in fact, the number is K. As a result, if the while-loop continues more than K times, 
        and haven't stopped, then we can conclude that remainder repeats -- 
        you can not have more than K different remainder.
        """
        if not k % 2 or not k % 5: 
            return -1
        
        rem = 0
        
        for i in range(1, k+1):
            
            rem = (rem*10 + 1) % k
            if not rem:
                return i
        
        return -1