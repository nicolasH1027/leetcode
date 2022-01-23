class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        cnt = collections.Counter(nums)
        
        prev, cur = 0, 0
        
        for val in range(max(cnt.keys()) + 1):
            
            prev, cur = cur, max(val*cnt[val] + prev, cur)
        
        return cur