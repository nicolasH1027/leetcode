class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        (a + b) % k  = 0
        ==
        (a%k + b%k) % k = 0
        
        ----------->>
        
        a % k = 0
        b % k = 0
        
        or
        
        a % k + b % k = 60
        
        """
        
        dic = collections.defaultdict(int)
        cnt = 0
        
        for val in time:
            if not val % 60:
                cnt += dic[0]
            else:
                cnt += dic[60 - val%60]
            dic[val%60] += 1
        
        return cnt