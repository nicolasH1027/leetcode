class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        prev = -inf
        for start, end in sorted(intervals, key = lambda x: x[1]):
            if start < prev:
                return False

            prev = end
        
        return True