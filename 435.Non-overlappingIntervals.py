class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        
        cnt = 0
        prev = -float('inf')
        for item in intervals:
            if item[0] >= prev:
                cnt += 1
                prev = item[1]
        return len(intervals) - cnt