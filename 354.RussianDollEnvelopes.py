class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))      
        
        top = []
        
        for num in envelopes:
            
            pos = bisect.bisect_left(top, num[1])
            
            if pos == len(top):
                top.append(num[1])
                
            else:
                top[pos] = num[1]
        
        return len(top)
    
    

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))     
        
        dp = [1]*len(envelopes)
        
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)