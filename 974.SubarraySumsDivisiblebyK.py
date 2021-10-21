class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        "same prefix sum procedure"
        seen = {0:1}
        cnt = 0
        cumod = 0
        
        # for val in nums:
        #     cumod += val
        #     cnt += seen.get((cumod%k + k)%k, 0)
        #     seen[(cumod%k + k)%k] = seen.get((cumod%k + k)%k, 0) + 1
        
        "(cumod + val) % k in other language,this part might be negative, then we use (cumod%k + k)%k this trick to make it positive"
        for val in nums:
            cumod = (cumod + val) % k
            cnt += seen.get(cumod, 0)
            seen[cumod] = seen.get(cumod, 0) + 1
        
        return cnt