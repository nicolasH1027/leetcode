class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        MaxDist, prev = 0, -1

        for i, val in enumerate(seats):
            
            if val:
                width = i if prev < 0 else (i - prev) // 2 # copy from lee215, clever way to handle the edge case
                MaxDist = max(MaxDist, width)
                prev = i
                
        
        return max(MaxDist, i - prev)