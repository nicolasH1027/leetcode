class Solution:
    """
    O(N) for both
    """
    def __init__(self, w: List[int]):
        self.total = 0
        self.cumsum = []
        for val in w:
            self.total += val
            self.cumsum.append(self.total)

    def pickIndex(self) -> int:
        target = self.total*random.random()
        for i, cumsum in enumerate(self.cumsum):
            if target <= cumsum:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class Solution:
    """
    O(N) for init, O(Nlog(N)) for pick
    """
    def __init__(self, w: List[int]):
        self.total = 0
        self.cumsum = []
        for val in w:
            self.total += val
            self.cumsum.append(self.total)

    def pickIndex(self) -> int:
        target = self.total*random.random()
        
        left, right = 0, len(self.cumsum) - 1
        
        while left < right:
            mid = left + (right - left)//2
            if self.cumsum[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return left
                 
