class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For monotonic stack, if we need to calculate the next greater number, then we need monotonic increasing stack
         if we need to calculate the next smaller number, then we need monotonic decreasing stack
         4 3 2 1 5, increasing stack
        """
        n = len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        return ans