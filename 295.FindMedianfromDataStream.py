class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        
        bisect.insort_left(self.data, num)
        
    def findMedian(self) -> float:
        n = len(self.data)
        
        return (self.data[n//2] + self.data[(n-1)//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        while len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi)) 

    def findMedian(self) -> float:
        
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) * 0.5
        else:
            return -self.lo[0]