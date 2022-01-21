class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        cnt = 0
        ages.sort()
        
        for val in ages:
            
            lo = bisect.bisect_left(ages, val // 2 + 8)
            
            hi = bisect.bisect_right(ages, val)
            
            cnt += max(hi - lo - 1, 0)
            
        return cnt
    
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        cnt = [0]*121
        for age in ages:
            cnt[age] += 1
        
        prev = [0]*121
        for i in range(1, 121):
            prev[i] = prev[i-1] + cnt[i]
            
        ans = 0
        
        for i in range(15, 121):
            
            if cnt[i]:
                
                ans += (prev[i] - prev[i//2 + 7] - 1)*cnt[i]
                
        return ans
            