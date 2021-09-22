class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        cause we are required to return the number itself not the index,
        so we can use sort() before. 
        """
        def twosum(nums,target):
            lo, hi = 0, len(nums) - 1
            result = []
            while lo < hi:
                tmp = nums[lo] + nums[hi]
                if tmp < target:
                    lo += 1
                elif tmp > target:
                    hi -= 1
                else:
                    result.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
            return result
        
        def ksum(nums, target, k):
            if not nums or nums[0]*k > target or nums[-1]*k < target:
                return []

            if k == 2:
                return twosum(nums, target)
            
            result = []

            n = len(nums)
            for i in range(n - k +1):
                if i  and nums[i] == nums[i - 1]: continue
                for item in ksum(nums[i+1:], target - nums[i], k - 1):
                    result.append([nums[i]] + item)
                    
            return result
        nums.sort()
        return ksum(nums, 0, 3)
       
            


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        "Two Pointers"
        nums.sort()
        result = []
        n = len(nums)
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i-1]: continue
            
            lo, hi = i+1, n-1
            while lo < hi:
                if nums[lo] + nums[hi] > -nums[i]:
                    hi -= 1
                elif nums[lo] + nums[hi] < -nums[i]:
                    lo += 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
        return result



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        "Hash set"
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            elif i and nums[i] == nums[i-1]: continue
            lo = i + 1
            seen = set()
            while lo < n:
                complement = -nums[i] - nums[lo]
                if complement in seen:
                    result.append([nums[i], nums[lo], complement])
                    while lo + 1 < n  and  nums[lo] == nums[lo+1]:
                        lo +=1
                seen.add(nums[lo])
                lo += 1
        return result


    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        No sort with hashmap and hashset
        
        The algorithm didnt fully prune the repeated value, so we need one 
        more hashset to record the value, which makes it difficult to figure
        out the logic behind it
        """
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for _, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res