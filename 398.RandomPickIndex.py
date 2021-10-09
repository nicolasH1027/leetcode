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