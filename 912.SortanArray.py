class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        MAX = max(nums)
        MIN = min(nums)
        
        count = [0]*(MAX - MIN + 1)
        
        for item in nums:
            count[item - MIN] += 1
        
        for i in range(1, len(count)):
            count[i] = count[i] + count[i-1]
        
        tmp = [0]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            pos = nums[i] - MIN
            cumSUM = count[pos]
            tmp[cumSUM - 1] = nums[i]
            count[pos] -= 1
            
        return tmp