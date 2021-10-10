class Solution:

    def __init__(self, nums: List[int]):
        """
        very straight forward
        """
        self.cache = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.cache [num].append(i)
        
    def pick(self, target: int) -> int:
        n = len(self.cache[target])
        return self.cache[target][random.randint(0, n-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution:

    def __init__(self, nums: List[int]):
        """
        Reservoir Sampling
        """
        self.nums = nums
        
    def pick(self, target: int) -> int:
        
        idx = 0
        count = 0
        for i, val in enumerate(self.nums):
            if val == target:
                count += 1
                if random.randint(0, count-1) == 0:
                    idx = i
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)