class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        right, i = 0, 0
        
        ans = 0
        
        for _, end in intervals:
            
            if end <= right:
                ans += 1
            else:
                right = end
        
        return len(intervals) - ans