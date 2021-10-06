class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        prev = 0
        maxheight = -inf
        for cut in horizontalCuts:
            maxheight = max(maxheight, cut - prev)
            prev = cut
        maxheight = max(maxheight, h - prev)
        print(maxheight)

        verticalCuts.sort()
        prev = 0
        maxlength = -inf
        for cut in verticalCuts:
            maxlength = max(maxlength, cut - prev)
            prev = cut
        maxlength = max(maxlength, w - prev)
        print(maxlength)
        
        return maxlength*maxheight % (10**9 + 7)