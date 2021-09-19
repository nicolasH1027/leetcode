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