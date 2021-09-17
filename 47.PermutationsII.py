import collections

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        'using counter'
        def backtracking(counter, track):
            if len(track) == len(nums):
                result.append(track[:])
                return 
            for item in counter:
                if counter[item] <= 0:
                    continue
                track.append(item)
                counter[item] -= 1
                backtracking(counter, track)
                track.pop()
                counter[item] += 1
        counter = collections.Counter(nums)
        result = []
        backtracking(counter, [])
        return result

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        'index'
        
        # [1a, 1b, 2a]
        # [1b, 1a, 2a]
        # so we need to check nums[i] == num[i-1] and flag[i - 1] == True        
       
        def backtracking(track, flag):
            
            if len(track) == len(nums):
                result.append(track[:])
                return
            
            for i in range(0, len(nums)):
                if flag[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not flag[i-1]:
                    continue
                flag[i] = True
                track.append(nums[i])
                backtracking(track, flag)
                track.pop()
                flag[i] = False
        flag = [False]*len(nums)
        result = []
        nums.sort()
        backtracking([], flag)
        return result