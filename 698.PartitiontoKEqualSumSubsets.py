class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tol = sum(nums)
        if tol % k != 0:
            return False
        
        mean = tol // k
        freq = [1]*len(nums)
        nums.sort(reverse = True)
        
        @lru_cache
        def backtrack(ind, part, cnt):

            if cnt == k-1:
                return True
            
            for i in range(ind, len(nums)):
                if freq[i] == 0: continue
                curSum = part + nums[i]
                if curSum > mean: continue
                if curSum == mean:
                    freq[i] -= 1
                    if backtrack(0, 0, cnt+1):
                        return True
                    freq[i] += 1
                if  curSum < mean:
                    freq[i] -= 1
                    if backtrack(ind+1, curSum, cnt):
                        return True
                    freq[i] += 1
    
        return backtrack(0, 0, 0)
                
                
            
            
        