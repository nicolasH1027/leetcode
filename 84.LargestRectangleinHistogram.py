class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        "monotonic stack application"
        heights.append(0)  # make sure the last element can be calculated
        n = len(heights)
        stack = [-1] # this will always points to 0 that added at line 5
        max_area = 0
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                start = stack[-1] if stack else -1
                max_area = max(max_area, heights[cur] * (i - start - 1))
            stack.append(i)
            
        return max_area