class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = [(num[0], i, 0) for i, num in enumerate(nums)]
        maxval = max([num[0] for num in nums])
        heapq.heapify(heap)
        left, right = -float('inf'), float('inf')
        
        while heap:
            minval, ind, loc = heapq.heappop(heap)
            
            if maxval - minval < right - left:
                left, right = minval, maxval
            
            if loc + 1 == len(nums[ind]):
                break
            
            maxval = max(maxval, nums[ind][loc+1])
            heapq.heappush(heap, (nums[ind][loc+1], ind, loc+1))
        
        return [left, right]
            