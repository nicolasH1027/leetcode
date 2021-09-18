class Solution:
    def maxArea(self, height: List[int]) -> int:
        "O(n)"
        maxarea = 0
        begin, end = 0, len(height) - 1
        while begin < end:
            maxarea = max(maxarea, min(height[begin], height[end])*(end - begin))  
            if height[begin]<= height[end]:
                begin += 1
                
            else:
                end -= 1
        return maxarea