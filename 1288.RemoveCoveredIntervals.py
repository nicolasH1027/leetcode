class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        left, right, i = intervals[0][0], intervals[0][1], 0
        
        ans = 0
        
        for start, end in intervals:
            
            if end <= right:
                ans += 1
            else:
                left = start
                right = end
        
        return len(intervals) - ans
            