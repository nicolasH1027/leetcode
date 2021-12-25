class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        def atmostk(nums, k):
        
            need = {}

            i, j, n = 0, 0, len(nums)

            ans = 0

            while i < n:

                need[nums[i]] = need.get(nums[i], 0) + 1
                i += 1

                while len(need) > k:

                    need[nums[j]] -= 1

                    if not need[nums[j]]:
                        del need[nums[j]]

                    j += 1
                    
                ans += i - j

            return ans
        
        return atmostk(nums, k) - atmostk(nums, k-1)