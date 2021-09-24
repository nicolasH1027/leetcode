class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        "sentinel  variable used here to avoid the check on boundary"
        timeSeries.append(10**8)
        result = 0
        for i in range(1, len(timeSeries)):
            result += min(timeSeries[i] - timeSeries[i-1], duration)
        return result