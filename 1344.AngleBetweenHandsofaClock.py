class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        res = abs((hour * 5 + (minutes/60) * 5) % 60 - minutes)*6
        
        
        return min(res, 360 -res)