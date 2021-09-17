class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        "call combination from 0 to n"
        def backtracking(start, track, k):
            if len(track) == k:
                result.append(track[:])
                return 
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtracking (i+1, track, k)
                track.pop()
        result = []
        for i in range(len(nums) + 1):
            backtracking(0, [], i)
        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        "smart way"
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output