class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x:x[1])
        
        cnt, prev = 0, -float('inf')
        
        for item in points:
            if item[0] > prev:
                cnt += 1
                prev = item[1]
                
        return cnt