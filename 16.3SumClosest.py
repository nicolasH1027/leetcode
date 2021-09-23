import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        "Template for K-sum cloest"
        "not the most efficient"
        def twosumclosest(nums, start, target):
            lo, hi = start, len(nums) - 1
            result = inf
            while lo < hi :
                T = nums[lo] + nums[hi]
                if T == target:
                    return T
                if abs(T - target) < abs(result - target):
                    result = T
                if T < target:
                    lo += 1
                else:
                    hi -= 1
            return result
                
        nums.sort()
        result = inf
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]: continue  # here, because we are computing the sum, so the repeated value
            tmp = nums[i] + twosumclosest(nums, i+1, target - nums[i])  # will result in the same value, so we remove it here.
            if abs(tmp - target) < abs(result - target):
                result = tmp
        return result
    
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        "more efficient one"
        n = len(nums)
        nums.sort()
        result = inf
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]: continue
            j, k = i + 1, n - 1
            while j < k:
                T = nums[i] + nums[j] + nums[k]
                if T == target:
                    return T
                if abs(T - target) < abs(result - target):
                    result = T
                if T < target:
                    j += 1
                else:
                    k -= 1
        return result

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        "Binary search"
        diff = inf
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i and nums[i] == num[i-1]: continue
            for j in range(i + 1, n):
                complement = target - nums[i] - nums[j]
                
                # insert 5a into   1,2,3,5,5,5b,6 -> 1,2,3,5,5,5b, 5a, 6
                # so in this case, we need to check 5b and 6
                hi = bisect.bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < n and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
                    
            if diff == 0:
                break
        return target - diff
        